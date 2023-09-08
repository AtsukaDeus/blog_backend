from django.urls import path
from .views import crear_publicacion

urlpatterns = [
    path('publicar', crear_publicacion, name='publicar'),
    
]