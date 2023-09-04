from django import forms

class Mensaje(forms.Form):
    sender=forms.CharField()
    reciever=forms.CharField()
    cuerpo_mensaje=forms.CharField(max_length=1000)
    fecha=forms.DateField(widget = forms.SelectDateWidget)