from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Publicacion
from .serializers import PublicacionSerializer 



@api_view(['POST'])
def crear_publicacion(request):
    if request.method == 'POST':
        data = request.data
        serializer = PublicacionSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def eliminar_publicacion(request):
    try:
        publicacion_id = request.data.get('id')
        if publicacion_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        publicacion = Publicacion.objects.get(pk=publicacion_id)
        publicacion.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    except Publicacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def obtener_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    serializer = PublicacionSerializer(publicaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)