from django.shortcuts import render
from AppBlog.views import *
from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

# Create your views here.

def perfil(request):
    return render(request, "AppLogin/perfil.html", {"avatar":obtenerAvatar(request)})

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
            return render(request, "AppLogin/login.html", {"formulario":form, "mensaje":"Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form=AuthenticationForm()
        return render(request, "AppLogin/login.html", {"formulario":form, "avatar":obtenerAvatar(request)})
    
def registrarse(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f'Usuario {nombre_usuario} se ha creado correctamente.', "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppLogin/registro.html", {"formulario":form, "mensaje":"Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form=RegistroUsuarioForm()
        return render(request, "AppLogin/registro.html", {"formulario":form, "avatar":obtenerAvatar(request)})
    
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  # Esto actualizará el nombre de usuario, correo electrónico y contraseña si se modifican
            return render(request, "AppLogin/perfil.html", {"mensaje": 'Perfil editado', "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppLogin/editarPerfil.html", {"formulario": form, "mensaje": 'Datos inválidos', "avatar":obtenerAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "AppLogin/editarPerfil.html", {"formulario": form, "avatar":obtenerAvatar(request)})
    
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, avatar=request.FILES['avatar'])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, 'AppLogin/perfil.html', {'mensaje':'Avatar agregado correctamente', 'avatar':obtenerAvatar})
        else:
            return render(request, 'AppLogin/agregarAvatar.html', {'form':form, 'usuario':request.user, 'mensaje':'Error al agregar nuevo avatar', 'avatar':obtenerAvatar})
    else:
        form=AvatarForm()
        return render(request, 'AppLogin/agregarAvatar.html', {'form':form, 'usuario':request.user, 'avatar':obtenerAvatar})
    
def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].avatar.url
    else:
        return '/media/avatares/Default_pfp.jpg'