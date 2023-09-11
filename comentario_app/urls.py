from django.urls import path
from .views import comentar_publicacion, comentar_respuesta, like_comentario, dislike_comentario

urlpatterns = [
    path('comentar_publicacion', comentar_publicacion, name='comentar_publicacion'),
    path('comentar_respuesta', comentar_respuesta, name='comentar_respuesta'),
    path('like_comentario', like_comentario, name='like_comentario'),
    path('dislike_comentario', dislike_comentario, name='dislike_comentario'),
]
