from django.urls import path
from .views import *

urlpatterns = [
    path('inbox/', inbox, name="inbox"),
    path('sentbox', sentbox, name="sentbox"),
    path('escribir', escribir, name='escribir'),
    path('eliminar/<pk>', MensajeDelete.as_view(), name='eliminar'),
    path('leer_mensaje/<pk>', MensajeDetalle.as_view(), name="leer_mensaje"),
]