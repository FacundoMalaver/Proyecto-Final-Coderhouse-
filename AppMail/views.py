from django.shortcuts import render, redirect
from AppLogin.views import *
from .forms import *
from .models import Mensajes
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def inbox(request):
    mensajes=Mensajes.objects.filter(recipiente=request.user)
    return render(request, "AppMail/inbox.html", {"mensajes":mensajes, "avatar":obtenerAvatar(request)})

@login_required
def sentbox(request):
    mensajes=Mensajes.objects.filter(emisario=request.user)
    return render(request, "AppMail/sentbox.html", {"avatar":obtenerAvatar(request), "mensajes":mensajes})

@login_required
def escribir(request):
    if request.method=="POST":
        form=MensajeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            recipiente=info["recipiente"]
            asunto=info['asunto']
            cuerpo_mensaje=info["cuerpo_mensaje"]
            fecha=info["fecha"]
            mensajes=Mensajes(asunto=asunto, cuerpo_mensaje=cuerpo_mensaje, fecha=fecha, emisario=request.user, recipiente=recipiente)
            mensajes.save()
            mensaje="Mensaje Enviado"
        else:
            mensaje="Datos invalidos"
        mensajes=Mensajes.objects.filter(emisario=request.user)
        return render(request, "AppMail/sentbox.html", {"mensaje":mensaje, "mensajes":mensajes, "avatar":obtenerAvatar(request)})
    else:
        formulario=MensajeForm()
    return render(request, "AppMail/escribir.html", {"formulario":formulario, "avatar":obtenerAvatar(request)})


class MensajeDelete(DeleteView, LoginRequiredMixin):
    model=Mensajes
    template_name="AppMail/eliminar.html"
    success_url = reverse_lazy('sentbox')

class MensajeDetalle(DetailView):
    model=Mensajes
    template_name="AppMail/leer_mensaje.html"