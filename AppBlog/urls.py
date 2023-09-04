from django.urls import path, include
from .views import *

urlpatterns = [
        path('reseñas/', reseñas, name="reseñas"),
        path('reseña/<pk>', ReseñaDetalle.as_view(), name="reseña_detalle"),
        path('busqueda/', busqueda, name='busqueda'),
        path('acercaDeMi/', acercaDeMi, name='acercaDeMi'),

        path('reseña_form/', agregar, name="reseña_form"),
        path('editarReseña/<pk>', ReseñaUpdate.as_view(), name="editarReseña"),
        path('eliminarReseña/<id>', eliminarReseña, name="eliminarReseña"),

        path('AppLogin', include('AppLogin.urls')),
        path('AppMail', include('AppMail.urls')),
]