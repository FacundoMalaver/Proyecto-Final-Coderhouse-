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

class UserEditForm(UserChangeForm):
    email=forms.EmailField(label="Modificar E-mail")
    
    class Meta:
        model=User
        fields=["username", "email"]
        help_texts={k:"" for k in fields}