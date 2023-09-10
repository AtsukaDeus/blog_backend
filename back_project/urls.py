from django.urls import path, include 

urlpatterns = [
    path('', include('admin_app.urls')),
    path('', include('publicacion_app.urls')),
    path('', include('usuario_app.urls')),
    path('', include('comentario_app.urls')),
    
]
