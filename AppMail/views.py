from django.shortcuts import render
from AppLogin.views import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def inbox(request):
    return render(request, "AppMail/inbox.html", {"avatar":obtenerAvatar(request)})

def sentbox(request):
    return render(request, "AppMail/sentbox.html", {"avatar":obtenerAvatar(request)})

def escribir(request):
    return render(request, "AppMail/escribir.html", {"avatar":obtenerAvatar(request)})