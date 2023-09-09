from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def registrar_usuario(request):

    username = request.data.get('username', None)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El nombre de usuario ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def iniciar_sesion(request):

    username = request.data.get('username', '')
    password = request.data.get('password', '')

    usuario = authenticate(request, username=username, password=password)

    if usuario is not None:
        login(request, usuario)
        return Response({'mensaje': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)





