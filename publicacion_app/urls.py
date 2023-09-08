from django.urls import path
from .views import crear_publicacion, eliminar_publicacion, obtener_publicaciones

urlpatterns = [
    path('crear_publicacion', crear_publicacion, name='crear_publicacion'),
    path('eliminar_publicacion', eliminar_publicacion, name='eliminar_publicacion'),
    path('obtener_publicaciones', obtener_publicaciones, name='obtener_publicaciones'),
    
]