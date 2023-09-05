from django import forms
from django.contrib.auth.models import User
from .models import Mensajes

class MensajeForm(forms.Form):
    recipiente=forms.ModelChoiceField(queryset=User.objects.all())
    asunto=forms.CharField(max_length=100)
    cuerpo_mensaje=forms.CharField(max_length=1000, widget=forms.Textarea)
    fecha=forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model=Mensajes
        exclude=['emisario', 'leido', 'estado']