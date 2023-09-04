from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inbox/', inbox, name="inbox"),
    path('sentbox/', sentbox, name="sentbox"),
    path('escribir', escribir, name='escribir')
]