from django.db import models
from django.contrib.auth.models import User
from publicacion_app.models import Publicacion


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    texto = models.TextField()
    fecha_creacion_comentario = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comentario_padre = models.ForeignKey('self', null=True, blank=True, related_name='respuestas', on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username}"

    class Meta:
        ordering = ['fecha_creacion_comentario']
    