from rest_framework import serializers
from .models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    autor_publicacion = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Publicacion
        fields = ('id', 'autor_publicacion', 'asunto', 'comentario', 'likes')