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
    return render(request, "AppBlog/inicio.html", {"avatar":obtenerAvatar(request)})

def acercaDeMi(request):
    return render(request, "AppBlog/acercaDeMi.html", {"avatar":obtenerAvatar(request)})

def perfil(request):
    return render(request, "AppBlog/perfil.html", {"avatar":obtenerAvatar(request)})

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
            autor=info["autor"]
            cuerpo=info["cuerpo"]
            imagen=info["imagen"]
            reseñas=Reseña(titulo=titulo, subtitulo=subtitulo, fecha=fecha, autor=autor, cuerpo=cuerpo, imagen=imagen)
            reseñas.save()
            mensaje="Reseña guardada"
        else:  
            mensaje=form.errors.as_data()
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
                return render(request, "AppBlog/inicio.html", {"mensaje":'Se ha inciado sesion.', "avatar":obtenerAvatar(request)})
        else: 
            return render(request, "AppBlog/login.html", {"formulario":form, "mensaje":"Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form=AuthenticationForm()
        return render(request, "AppBlog/login.html", {"formulario":form, "avatar":obtenerAvatar(request)})
    
def registrarse(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f'Usuario {nombre_usuario} se ha creado correctamente.', "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppBlog/registro.html", {"formulario":form, "mensaje":"Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form=RegistroUsuarioForm()
        return render(request, "AppBlog/registro.html", {"formulario":form, "avatar":obtenerAvatar(request)})
    
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  # Esto actualizará el nombre de usuario, correo electrónico y contraseña si se modifican
            return render(request, "AppBlog/perfil.html", {"mensaje": 'Perfil editado', "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppBlog/editarPerfil.html", {"formulario": form, "mensaje": 'Datos inválidos', "avatar":obtenerAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "AppBlog/editarPerfil.html", {"formulario": form, "avatar":obtenerAvatar(request)})

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

def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].avatar.url
    else:
        return '/media/avatares/Default_pfp.jpg'
    
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, avatar=request.FILES['avatar'])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, 'AppBlog/perfil.html', {'mensaje':'Avatar agregado correctamente', 'avatar':obtenerAvatar})
        else:
            return render(request, 'AppBlog/agregarAvatar.html', {'form':form, 'usuario':request.user, 'mensaje':'Error al agregar nuevo avatar', 'avatar':obtenerAvatar})
    else:
        form=AvatarForm()
        return render(request, 'AppBlog/agregarAvatar.html', {'form':form, 'usuario':request.user, 'avatar':obtenerAvatar})