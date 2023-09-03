from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.dispatch import Signal

model_delete_signal = Signal()

class ReseñasForm(forms.Form):
    titulo=forms.CharField(max_length=50, help_text="max. 50 caracteres")
    subtitulo=forms.CharField(max_length=100, help_text="max. 100 caracteres", widget=forms.Textarea)
    fecha=forms.DateField(widget = forms.SelectDateWidget)
    autor=forms.CharField(max_length=20)
    cuerpo=forms.CharField(max_length=1000, help_text="max. 1000 caracteres", widget=forms.Textarea)
    imagen=forms.ImageField()

class RegistroUsuarioForm(UserCreationForm):
    username=forms.CharField(label="Usuario")
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Agregue una descricion personal (opcional)", max_length=200, required=False, widget=forms.Textarea)
    last_name=forms.CharField(label="Agregue un link a su pagina web (opcional)", required=False)

    class Meta:
        model=User
        fields=["username", "email", "first_name", "last_name"]
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar=forms.ImageField(label="Imagen")