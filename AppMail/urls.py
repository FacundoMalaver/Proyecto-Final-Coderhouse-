from django.urls import path
from .views import *

urlpatterns = [
    path('inbox/', inbox, name="inbox"),
    path('sentbox/', sentbox, name="sentbox"),
    path('escribir', escribir, name='escribir')
]