from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppBlog/inicio.html")

def reseñas(request):
    return render(request, "AppBlog/reseñas.html")

def introduccion(request):
    return render(request, "AppBlog/introduccion.html")

def agregar(request):
    if request.method=="POST":
        form=ReseñasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            titulo=info["titulo"]
            subtitulo=info["subtitulo"]
            fecha=info["fecha"]
            autor=info["autor"]
            reseña=Reseña(titulo=titulo,subtitulo=subtitulo,fecha=fecha,autor=autor)
            reseña.save()
            mensaje="Reseña guardada"
        else:
            mensaje="Datos invalidos"
        formulario_reseñas=ReseñasForm()
        return render(request, "AppBlog/agregar.html", {"mensaje":mensaje, "formulario":formulario_reseñas})
    else:
        formulario_reseñas=ReseñasForm()
    return render(request, "AppBlog/agregar.html", {"formulario":formulario_reseñas})