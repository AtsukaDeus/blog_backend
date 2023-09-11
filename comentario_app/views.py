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
def comentar_publicacion(request):
    publicacion_id = request.data.get('publicacion_id')
    if publicacion_id is None:
        return Response({'error':'se debe proporcionar publicacion_id'},status=status.HTTP_400_BAD_REQUEST)
    
    try:
        publicacion = Publicacion.objects.get(id=publicacion_id)
    
    except Publicacion.DoesNotExist:
        return Response({'error':'La publicacion no existe!'}, status=status.HTTP_404_NOT_FOUND)  
        
    data = request.data
    data['publicacion'] = publicacion.id
    data['usuario'] = request.user.id #<- obtiene directamente el usuario al estar loggeado

    serializer = ComentarioSerializer(data=data)

    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comentar_respuesta(request):
    comentario_padre_id = request.data.get('comentario_padre_id')
    publicacion_id = request.data.get('publicacion_id')
    if publicacion_id is None:
        return Response({'error':'se debe proporcionar publicacion_id'},status=status.HTTP_400_BAD_REQUEST)

    if comentario_padre_id is None:
        return Response({'error':'se debe proporcionar comentario_padre_id'},status=status.HTTP_400_BAD_REQUEST)
    
    try:
        publicacion = Publicacion.objects.get(id=publicacion_id)
    
    except Publicacion.DoesNotExist:
        return Response({'error':'La publicacion no existe!'}, status=status.HTTP_404_NOT_FOUND) 
    
    try:
        comentario = Comentario.objects.get(id=comentario_padre_id)
    
    except Publicacion.DoesNotExist:
        return Response({'error':'El comentario no existe!'}, status=status.HTTP_404_NOT_FOUND) 
    

    data = request.data
    data['comentario_padre'] = comentario_padre.id
    data['publicacion'] = publicacion.id
    data['usuario'] = request.user.id

    serializer = ComentarioSerializer(data=data)

    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def like_comentario(request):
    try:
        comentario_id = request.data.get('id')
        if comentario_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try: 
            comentario = Comentario.objects.get(id=comentario_id)
        
        except Comentario.DoesNotExist:
            return Response({'error':'El comentario no existe!'}, status=status.HTTP_404_NOT_FOUND)    
        
        comentario.likes += 1
        comentario.save()
        
        return Response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def dislike_comentario(request):
    try:
        comentario_id = request.data.get('id')
        if comentario_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try: 
            comentario = Comentario.objects.get(id=comentario_id)
        
        except Comentario.DoesNotExist:
            return Response({'error':'El comentario no existe!'}, status=status.HTTP_404_NOT_FOUND)    
        
        comentario.likes -= 1
        comentario.save()
        
        return Response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)