from django import forms

class ReseñasForm(forms.Form):
    titulo=forms.CharField(max_length=50, help_text="max. 50 caracteres")
    subtitulo=forms.CharField(max_length=100, help_text="max. 100 caracteres")
    fecha=forms.DateField(help_text="eg.:'2006-10-25', '10/25/2006' o '10/25/06'")
    autor=forms.CharField(max_length=10)
    cuerpo=forms.CharField(max_length=1000, help_text="max. 1000 caracteres")
