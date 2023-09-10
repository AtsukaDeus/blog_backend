from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Publicacion, Comentario
from .serializers import ComentarioSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_comentario(request):
    publicacion_id = request.data.get('publicacion')
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)

    data = request.data
    data['publicacion'] = publicacion.id
    data['usuario'] = request.user.id #<- obtiene directamente el usuario al estar loggeado

    serializer = ComentarioSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_comentario_respuesta(request):
    comentario_padre_id = request.data.get('comentario')
    comentario_padre = get_object_or_404(Comentario, pk=comentario_padre_id)

    data = request.data
    data['comentario_padre'] = comentario_padre.id
    data['usuario'] = request.user.id

    serializer = ComentarioSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

