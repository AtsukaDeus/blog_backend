from django.db import models

# Create your models here.

class Publicacion(models.Model):
    asunto = models.CharField(max_length=255)
    comentario = models.TextField()

    def __str__(self):
        return self.asunto