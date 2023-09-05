from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from AppLogin.views import *

# Create your views here.
def inicio(request):
    return render(request, "AppBlog/inicio.html", {"avatar":obtenerAvatar(request)})

def acercaDeMi(request):
    return render(request, "AppBlog/acercaDeMi.html", {"avatar":obtenerAvatar(request)})

def reseñas(request):
    reseñas=Reseña.objects.all()
    return render(request, "AppBlog/reseñas.html", {"reseñas":reseñas, "avatar":obtenerAvatar(request)})

@login_required
def agregar(request):
    if request.method=="POST":
        form=ReseñasForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            titulo=info["titulo"]
            subtitulo=info["subtitulo"]
            fecha=info["fecha"]
            cuerpo=info["cuerpo"]
            imagen=info["imagen"]
            reseñas=Reseña(titulo=titulo, subtitulo=subtitulo, fecha=fecha, autor=request.user, cuerpo=cuerpo, imagen=imagen)
            reseñas.save()
            mensaje="Reseña guardada"
        else:  
            mensaje="Datos invalidos"
        reseñas=Reseña.objects.all()
        return render(request, "AppBlog/reseñas.html", {"mensaje":mensaje, "reseñas":reseñas, "avatar":obtenerAvatar(request)})
    else:
        formulario=ReseñasForm()
    return render(request, "AppBlog/reseña_form.html", {"formulario":formulario, "avatar":obtenerAvatar(request)})

@login_required
def eliminarReseña(request, id):
    reseña=Reseña.objects.get(id=id)
    reseña.delete()
    reseñas=Reseña.objects.all()
    mensaje="Reseña eliminada"
    return render(request, "AppBlog/reseñas.html", {"reseñas":reseñas, "mensaje":mensaje, "avatar":obtenerAvatar(request)})


class ReseñaUpdate(UpdateView, LoginRequiredMixin):
    model=Reseña
    template_name="AppBlog/editarReseña.html"
    success_url=reverse_lazy("reseñas")
    fields= ['titulo', 'subtitulo', 'cuerpo','fecha', 'autor', 'imagen']

class ReseñaDetalle(DetailView):
    model=Reseña
    template_name="AppBlog/reseña_detalle.html"

def busqueda(request):
    if request.method == 'GET':
        titulo= request.GET.get('titulo')
        submitbutton= request.GET.get('submit')
        if titulo is not None:
            reseñas=Reseña.objects.filter(titulo__icontains=titulo)
            return render(request, 'AppBlog/busqueda.html', {'reseñas':reseñas, 'submitbutton':submitbutton, "avatar":obtenerAvatar(request)})
        else:
            return render(request, 'AppBlog/busqueda.html', {"avatar":obtenerAvatar(request)})
    else:
        return render(request, 'AppBlog/busqueda.html', {"avatar":obtenerAvatar(request)})


    
