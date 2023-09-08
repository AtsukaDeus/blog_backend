from django.urls import path
from .views import crear_publicacion, eliminar_publicacion

urlpatterns = [
    path('crear_publicacion', crear_publicacion, name='crear_publicacion'),
    path('eliminar_publicacion', eliminar_publicacion, name='eliminar_publicacion'),
    
]