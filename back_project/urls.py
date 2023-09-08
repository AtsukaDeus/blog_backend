from django.urls import path

urlpatterns = [
    path('', include('admin_app.urls')),
    path('', include('publicacion_app.urls')),
    path('', include('usuario.urls')),
    
]
