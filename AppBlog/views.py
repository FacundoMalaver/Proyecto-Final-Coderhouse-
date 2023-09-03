from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request, "AppBlog/inicio.html")

def perfil(request):
    return render(request, "AppBlog/perfil.html")

def reseñas(request):
    reseñas=Reseña.objects.all()
    return render(request, "AppBlog/reseñas.html", {"reseñas":reseñas})

def introduccion(request):
    return render(request, "AppBlog/introduccion.html")

@login_required
def agregar(request):
    if request.method=="POST":
        form=ReseñasForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            titulo=info["titulo"]
            subtitulo=info["subtitulo"]
            fecha=info["fecha"]
            autor=info["autor"]
            cuerpo=info["cuerpo"]
            imagen=info["imagen"]
            reseñas=Reseña(titulo=titulo, subtitulo=subtitulo, fecha=fecha, autor=autor, cuerpo=cuerpo, imagen=imagen)
            reseñas.save()
            mensaje="Reseña guardada"
        else:  
            mensaje=form.errors.as_data()
        reseñas=Reseña.objects.all()
        return render(request, "AppBlog/reseñas.html", {"mensaje":mensaje, "reseñas":reseñas})
    else:
        formulario=ReseñasForm()
    return render(request, "AppBlog/reseña_form.html", {"formulario":formulario})

@login_required
def eliminarReseña(request, id):
    reseña=Reseña.objects.get(id=id)
    reseña.delete()
    reseñas=Reseña.objects.all()
    mensaje="Reseña eliminada"
    return render(request, "AppBlog/reseñas.html", {"reseñas":reseñas, "mensaje":mensaje})


class ReseñaUpdate(UpdateView, LoginRequiredMixin):
    model=Reseña
    template_name="AppBlog/editarReseña.html"
    success_url=reverse_lazy("reseñas")
    fields= ['titulo', 'subtitulo', 'cuerpo','fecha', 'autor', 'imagen']

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
    
def registrarse(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f'Usuario {nombre_usuario} se ha creado correctamente.'})
        else:
            return render(request, "AppBlog/registro.html", {"formulario":form, "mensaje":"Datos invalidos"})
    else:
        form=RegistroUsuarioForm()
        return render(request, "AppBlog/registro.html", {"formulario":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            info=form.cleaned_data
            email=info["email"]
            password1=info["password1"]
            password2=info["password2"]
            usuario=User(email=email, password1=password1, password2=password2)
            usuario.save()
            return render(request, "AppBlog/perfil.html", {"mensaje":'Perfil editado'})
        else:
            return render(request, "AppBlog/editarPerfil.html", {"formulario":form, "mensaje":'Datos invalidos'})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppBlog/editarPerfil.html", {"formulario":form})

def busqueda(request):
    if request.method == 'GET':
        titulo= request.GET.get('titulo')
        submitbutton= request.GET.get('submit')
        if titulo is not None:
            reseñas=Reseña.objects.filter(titulo__icontains=titulo)
            return render(request, 'AppBlog/busqueda.html', {'reseñas':reseñas, 'submitbutton':submitbutton})
        else:
            return render(request, 'AppBlog/busqueda.html')
    else:
        return render(request, 'AppBlog/busqueda.html')
