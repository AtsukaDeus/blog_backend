from django.urls import path
from .views import registrar_usuario, iniciar_sesion, cerrar_sesion


urlpatterns = [
    path('registrar_usuario', registrar_usuario, name='registrar_usuario'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
]
