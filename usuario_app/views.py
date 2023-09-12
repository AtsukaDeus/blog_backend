from django.shortcuts import render
from django.contrib.auth import authenticate, login, password_validation, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([AllowAny])
def registrar_usuario(request):
    username = request.data.get('username', None)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El nombre de usuario ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

    password = request.data.get('password')

    try:
        password_validation.validate_password(password)
        
    except password_validation.ValidationError as errors:
        return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST) #<- muestra los errores de la contraseña

    user = User.objects.create(username=username)
    user.set_password(password) #cifrando password con set_password
    user.save()

    return Response({'mensaje': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([AllowAny])
def iniciar_sesion(request):

    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(request, username=username, password=password)

    if usuario is not None:
        # Autenticación exitosa, ahora vamos a generar un token para el usuario
        token, created = Token.objects.get_or_create(user=usuario)
        return Response({'token': token.key, 'mensaje': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def cerrar_sesion(request):
    logout(request)
    return Response({'mensaje': 'Cierre de sesión exitoso'}, status=status.HTTP_200_OK)



