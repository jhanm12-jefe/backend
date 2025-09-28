from django.shortcuts import render
from administracion.models import User, Rol
from administracion2.models import Ingrediente, Receta, PasoReceta, RecetaIngrediente, Historial, Favorito
from administracion2.serializers import (
    IngredienteSerializer, RecetaSerializer, PasoRecetaSerializer,
    RecetaIngredienteSerializer, HistorialSerializer, FavoritoSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET','POST'])
def crudIngrediente(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crudIngrediente_detail(request, id):
    try:
        ingrediente = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response("ingrediente no encontrado", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ingrediente.delete()
        return Response("eliminado con éxito")



@api_view(['GET','POST'])
def crudReceta(request):
    if request.method == 'GET':
        recetas = Receta.objects.all()
        serializer = RecetaSerializer(recetas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crudReceta_detail(request, id):
    try:
        receta = Receta.objects.get(pk=id)
    except Receta.DoesNotExist:
        return Response("receta no encontrada", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecetaSerializer(receta)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RecetaSerializer(receta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        receta.delete()
        return Response("eliminado con éxito")



@api_view(['GET','POST'])
def crudPasoReceta(request):
    if request.method == 'GET':
        pasos = PasoReceta.objects.all()
        serializer = PasoRecetaSerializer(pasos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PasoRecetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crudPasoReceta_detail(request, id):
    try:
        paso = PasoReceta.objects.get(pk=id)
    except PasoReceta.DoesNotExist:
        return Response("paso no encontrado", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PasoRecetaSerializer(paso)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PasoRecetaSerializer(paso, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        paso.delete()
        return Response("eliminado con éxito")



@api_view(['GET','POST'])
def crudRecetaIngrediente(request):
    if request.method == 'GET':
        relaciones = RecetaIngrediente.objects.all()
        serializer = RecetaIngredienteSerializer(relaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecetaIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crudRecetaIngrediente_detail(request, id):
    try:
        relacion = RecetaIngrediente.objects.get(pk=id)
    except RecetaIngrediente.DoesNotExist:
        return Response("relación no encontrada", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecetaIngredienteSerializer(relacion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RecetaIngredienteSerializer(relacion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        relacion.delete()
        return Response("eliminado con éxito")



@api_view(['GET','POST'])
def crudHistorial(request):
    if request.method == 'GET':
        historial = Historial.objects.all()
        serializer = HistorialSerializer(historial, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HistorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crudHistorial_detail(request, id):
    try:
        h = Historial.objects.get(pk=id)
    except Historial.DoesNotExist:
        return Response("historial no encontrado", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HistorialSerializer(h)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = HistorialSerializer(h, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        h.delete()
        return Response("eliminado con éxito")



@api_view(['GET','POST'])
def crudFavorito(request):
    if request.method == 'GET':
        favoritos = Favorito.objects.all()
        serializer = FavoritoSerializer(favoritos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FavoritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crudFavorito_detail(request, id):
    try:
        fav = Favorito.objects.get(pk=id)
    except Favorito.DoesNotExist:
        return Response("favorito no encontrado", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavoritoSerializer(fav)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FavoritoSerializer(fav, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        fav.delete()
        return Response("eliminado con éxito")

@api_view(['POST'])
def agregar_favorito(request, receta_id):
    usuario_id = request.data.get("usuario_id")

    try:
        usuario = User.objects.get(id=usuario_id)
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if not getattr(usuario, "es_premium", False):
        return Response({"error": "Solo los usuarios premium pueden agregar favoritos"}, status=status.HTTP_403_FORBIDDEN)

    try:
        receta = Receta.objects.get(id=receta_id)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    Favorito.objects.get_or_create(usuario=usuario, receta=receta)

    return Response({"mensaje": f"{receta.nombre} agregado a favoritos"})