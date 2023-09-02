from django.urls import path
from .views import *

urlpatterns = [
        path('reseñas', reseñas, name="reseñas"),
        path('introduccion', introduccion, name="introduccion"),
        path('agregar', agregar, name="agregar"),
        path('reseña/<pk>', ReseñaDetalle.as_view(), name="reseña_detalle"),
        path('login', iniciar_sesion, name='login')
]