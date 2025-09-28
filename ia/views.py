from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import json
import re

from administracion2.models import Receta, Ingrediente, RecetaIngrediente, PasoReceta, Historial

# Configuración API Google
API_KEY = "AIzaSyAaP_2YF435AvgSrbxxrwSZBYYdGXp296Q"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


# ============================
# 1️⃣ Generar receta (solo título)
# ============================
@api_view(['POST'])
def generar_receta(request):
    data = request.data
    ingredientes = data.get("ingredientes", [])
    usuario_id = data.get("usuario_id")  # Opcional

    if not ingredientes:
        return Response({"error": "Debes enviar al menos un ingrediente"}, status=status.HTTP_400_BAD_REQUEST)

    # Prompt solo para nombre de receta
    prompt = f"""
Eres un asistente de cocina para principiantes. Responde ÚNICAMENTE en JSON válido.
Usa esta estructura:
{{
  "nombre": "NOMBRE_DE_LA_RECETA"
}}
Solo puedes usar estos ingredientes: {', '.join(ingredientes)}
No incluyas sugerencias ni texto adicional.
"""

    response = model.generate_content(prompt)
    texto = response.text.strip()
    texto_limpio = re.sub(r"^```[a-zA-Z]*|```$", "", texto, flags=re.MULTILINE).strip()

    try:
        data_ia = json.loads(texto_limpio)
        nombre = data_ia.get("nombre", "Receta sin nombre")
    except json.JSONDecodeError:
        nombre = "Receta sin nombre"

    # Guardar receta en BD
    receta = Receta.objects.create(
        nombre=nombre,
        descripcion=f"Receta generada con {', '.join(ingredientes)}",
        tiempo_preparacion=0,
        tiempo_coccion=0
    )

    # Relacionar ingredientes
    for ing in ingredientes:
        ingrediente_obj, _ = Ingrediente.objects.get_or_create(nombre=ing, tipo="desconocido")
        RecetaIngrediente.objects.create(receta=receta, ingrediente=ingrediente_obj, cantidad="al gusto")

    # Guardar historial solo si hay usuario
    if usuario_id:
        Historial.objects.create(usuario_id=usuario_id, receta=receta)

    return Response({
        "id": receta.id,
        "nombre": receta.nombre
    })


# ============================
# 2️⃣ Obtener pasos de la receta
# ============================
@api_view(['GET'])
def detalle_receta(request, receta_id):
    try:
        receta = Receta.objects.get(id=receta_id)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    # Si ya tiene pasos guardados
    if receta.pasos.exists():
        pasos_texto = [p.descripcion for p in receta.pasos.all()]
        return Response({
            "id": receta.id,
            "nombre": receta.nombre,
            "ingredientes": [ri.ingrediente.nombre for ri in receta.ingredientes.all()],
            "pasos": pasos_texto
        })

    # Generar pasos con IA para principiantes
    ingredientes_txt = ", ".join([ri.ingrediente.nombre for ri in receta.ingredientes.all()])
    prompt = f"""
Eres un asistente de cocina para principiantes. Genera pasos detallados y fáciles de seguir
para preparar la receta '{receta.nombre}' usando únicamente estos ingredientes: {ingredientes_txt}.
Responde ÚNICAMENTE en JSON válido:
{{
  "pasos": [
    "Paso 1...",
    "Paso 2...",
    "Paso 3..."
  ]
}}
No incluyas explicaciones adicionales.
"""

    response = model.generate_content(prompt)
    texto = response.text.strip()
    texto_limpio = re.sub(r"^```[a-zA-Z]*|```$", "", texto, flags=re.MULTILINE).strip()

    try:
        data_ia = json.loads(texto_limpio)
        pasos_list = data_ia.get("pasos", [])
    except json.JSONDecodeError:
        pasos_list = [p.strip() for p in texto.split("\n") if p.strip()]

    # Guardar pasos en BD
    for i, paso in enumerate(pasos_list, start=1):
        PasoReceta.objects.create(receta=receta, numero=i, descripcion=paso)

    return Response({
        "id": receta.id,
        "nombre": receta.nombre,
        "ingredientes": [ri.ingrediente.nombre for ri in receta.ingredientes.all()],
        "pasos": pasos_list
    })