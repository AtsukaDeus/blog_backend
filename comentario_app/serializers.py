from rest_framework import serializers
from .models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    autor_comentario = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Comentario
        fields = ('id', 'texto', 'autor_comentario', 'fecha_creacion_comentario', 'likes', 'comentario_padre', 'publicacion')

