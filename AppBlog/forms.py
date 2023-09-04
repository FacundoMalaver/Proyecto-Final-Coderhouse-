from django import forms
from .models import Reseña
from django.dispatch import Signal

model_delete_signal = Signal()

class ReseñasForm(forms.Form):
    titulo=forms.CharField(max_length=50, help_text="max. 50 caracteres")
    subtitulo=forms.CharField(max_length=100, help_text="max. 100 caracteres", widget=forms.Textarea)
    fecha=forms.DateField(widget = forms.SelectDateWidget)
    cuerpo=forms.CharField(max_length=1000, help_text="max. 1000 caracteres", widget=forms.Textarea)
    imagen=forms.ImageField()

    class Meta:
        model=Reseña
        exclude=['autor']

