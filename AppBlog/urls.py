from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('reseñas/', reseñas, name="reseñas"),
        path('introduccion/', introduccion, name="introduccion"),
        path('reseña/<pk>', ReseñaDetalle.as_view(), name="reseña_detalle"),
        path('busqueda/', busqueda, name='busqueda'),

        path('reseña_form/', agregar, name="reseña_form"),
        path('editarReseña/<pk>', ReseñaUpdate.as_view(), name="editarReseña"),
        path('eliminarReseña/<id>', eliminarReseña, name="eliminarReseña"),

        path('login/', iniciar_sesion, name='login'),
        path('registro/', registrarse, name='registro'),
        path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

        path('editarPerfil/', editarPerfil, name='editarPerfil'),
        path('perfil', perfil, name='perfil')
]