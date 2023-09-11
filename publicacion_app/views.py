from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Publicacion
from .serializers import PublicacionSerializer 



@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def crear_publicacion(request):
    data = request.data
    data['usuario'] = request.user.id
    serializer = PublicacionSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def eliminar_publicacion(request):
    try:
        publicacion_id = request.data.get('id')
        if publicacion_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            publicacion = Publicacion.objects.get(pk=publicacion_id)
            
        except Publicacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

        if publicacion.usuario == request.user:
            publicacion.delete()
            return Response({'mensaje':'publicación eliminada'}, status=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@permission_classes([AllowAny])
def obtener_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    serializer = PublicacionSerializer(publicaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def like_publicacion(request):
    try:
        publicacion_id = request.data.get('id')
        if publicacion_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try: 
            publicacion = Publicacion.objects.get(id=publicacion_id)
        
        except Publicacion.DoesNotExist:
            return Response({'error':'La publicación no existe!'}, status=status.HTTP_404_NOT_FOUND)    
        
        publicacion.likes += 1
        publicacion.save()
        
        return Response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def dislike_publicacion(request):
    try:
        publicacion_id = request.data.get('id')
        if publicacion_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try: 
            publicacion = Publicacion.objects.get(id=publicacion_id)
        
        except Publicacion.DoesNotExist:
            return Response({'error':'La publicación no existe!'}, status=status.HTTP_404_NOT_FOUND)    
        
        publicacion.likes -= 1
        publicacion.save()
        
        return Response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)