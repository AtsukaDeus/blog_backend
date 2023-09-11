from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    asunto = models.CharField(max_length=255)
    detalle = models.TextField()
    likes = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_creacion_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto
    
    class Meta:
        ordering = ['fecha_creacion_publicacion']
    

