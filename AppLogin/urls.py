from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
        path('login/', iniciar_sesion, name='login'),
        path('registro/', registrarse, name='registro'),
        path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

        path('editarPerfil/', editarPerfil, name='editarPerfil'),
        path('perfil/', perfil, name='perfil'),
        path('agregarAvatar', agregarAvatar, name='agregarAvatar'),
        
]