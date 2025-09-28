from django.shortcuts import render
from administracion.models import Rol, User , Suscripcion
from administracion.serializers import RolSerializer,UserSerializer, SuscripcionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


@api_view(['GET'])
def prueba(request):
    respuesta = "hola mundo"
    return Response(respuesta)

@api_view(['GET','POST'])
def crudRol(request):
    if request.method == 'GET':
        rols = Rol.objects.all()
        serializer = RolSerializer(rols, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RolSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
@api_view(['GET','PUT','DELETE'])    
def crudRol_detail(request,id):
    try:
        rol = Rol.objects.get(pk = id)
    except Rol.DoesNotExist:
        return Response("rol no encontrado", status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RolSerializer(rol)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = RolSerializer(rol, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        rol.delete()
        return Response("eliminar con exito")
    

@api_view(['GET', 'POST'])
def crudUser(request):
    """
    GET: Lista todos los usuarios
    POST: Crea un nuevo usuario con rol 'usuario' por defecto
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        # Asignar el rol 'usuario' por defecto
        rol, created = Rol.objects.get_or_create(nombre='usuario')
        data['rol'] = rol.id

        # Hashear la contraseña antes de guardar
        if 'password' in data:
            data['password'] = make_password(data['password'])

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def crudUser_detail(request, id):
    """
    GET: Muestra un usuario por ID
    PUT: Actualiza un usuario por ID
    DELETE: Elimina un usuario por ID
    """
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"mensaje": "Usuario eliminado con éxito"})
    
@api_view(['GET','POST'])
def crudSuscripcion(request):
    if request.method == 'GET':
        suscripciones = Suscripcion.objects.all()
        serializer = SuscripcionSerializer(suscripciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def crudSuscripcion_detail(request, id):
    try:
        suscripcion = Suscripcion.objects.get(pk=id)
    except Suscripcion.DoesNotExist:
        return Response("suscripción no encontrada", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuscripcionSerializer(suscripcion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SuscripcionSerializer(suscripcion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        suscripcion.delete()
        return Response("eliminada con éxito")
    
@api_view(['GET'])
def showByRol(request,id):
    users = User.objects.filter(rol_id = id)
    cantidad = users.count()
    serializer = UserSerializer(users, many = True)

    
    diccionario = {
        "cantidad" : cantidad,
        "datos"    : serializer.data
    }
    return Response(diccionario)

@api_view(['GET'])
def BuscarPais(request):
    url = "https://restcountries.com/v3.1/name/bolivia"
    resp = requests.get(url)
    resp = resp.json()[0]
    print(resp.get("name"))
    return Response("exito")


# administracion/views.py
from django.http import JsonResponse

def prueba(request):
    data = {'mensaje': '¡Conexión exitosa desde el back-end!'}
    return JsonResponse(data)


@api_view(['POST'])
def loginUser(request):
    correo = request.data.get('correo')
    password = request.data.get('password')
    print("Request data:", request.data)

    if not correo or not password:
        return Response({"error": "Correo y contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(correo=correo)
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if check_password(password, user.password):
        return Response({
            "message": "Login exitoso",   # ✅ Aquí va el mensaje
            "user_id": user.id,
            "correo": user.correo,
            "rol": user.rol.nombre
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
