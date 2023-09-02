from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def inicio(request):
    return render(request, "AppBlog/inicio.html")

def reseñas(request):
    reseñas=Reseña.objects.all()
    return render(request, "AppBlog/reseñas.html", {"reseñas":reseñas})

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
            cuerpo=info["cuerpo"]
            reseña=Reseña(titulo=titulo,subtitulo=subtitulo, fecha=fecha ,autor=autor,cuerpo=cuerpo)
            reseña.save()
            mensaje="Reseña guardada"
        else:
            mensaje="Datos invalidos"
        reseñas=Reseña.objects.all()
        return render(request, "AppBlog/reseñas.html", {"mensaje":mensaje, "reseñas":reseñas})
    else:
        formulario_reseñas=ReseñasForm()
    return render(request, "AppBlog/agregar.html", {"formulario":formulario_reseñas})

def eliminar(request, id):
    reseña=Reseña.objects.get(id=id)
    reseña.delete()
    mensaje="Reseña eliminada"
    return render(request, "AppBlog/inicio.html", {"mensaje":mensaje})

def editar(request, id):
    reseña=Reseña.objects.get(id=id)
    if request.method=="POST":
        form=ReseñasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            reseña.titulo=info["titulo"]
            reseña.subtitulo=info["subtitulo"]
            reseña.fecha=info["fecha"]
            reseña.autor=info["autor"]
            reseña.cuerpo=info["cuerpo"]
            reseña.save()
            mensaje="Reseña editada"
            reseñas=Reseña.objects.all()
            return render(request, "AppBlog/reseñas.html", {"mensaje":mensaje, "reseñas":reseñas})
    else:
        formulario_reseña=ReseñasForm(instance=reseña)
        return render(request,"AppBlog/editar.html", {"formulario":formulario_reseña, "reseña":reseña})
    
class ReseñaDetalle(DetailView):
    model=Reseña
    template_name="AppBlog/reseña_detalle.html"

def iniciar_sesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlog/inicio.html", {"mensaje":'Se ha inciado sesion.'})
        else: 
            return render(request, "AppBlog/login.html", {"formulario":form, "mensaje":"Datos invalidos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppBlog/login.html", {"formulario":form})