from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    asunto = models.CharField(max_length=255)
    comentario = models.TextField()
    likes = models.IntegerField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.asunto
    

