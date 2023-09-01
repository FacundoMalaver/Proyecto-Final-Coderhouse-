from django.urls import path
from .views import *

urlpatterns = [
        path('reseñas', reseñas, name="reseñas"),
        path('introduccion', introduccion, name="introduccion"),
        path('agregar', agregar, name="agregar")
]