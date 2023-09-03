from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Reseña(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField(default=datetime.date.today)
    autor=models.CharField(max_length=20, default='Anonimo')
    cuerpo=models.CharField(max_length=1000)
    imagen=models.ImageField(upload_to='portadas')
    def __str__(self):
        return f'{self.titulo} - {self.fecha} - {self.autor}'

class Portada(models.Model):
    imagen=models.ImageField(upload_to='portadas')
    reseña=models.ForeignKey(Reseña, on_delete=models.CASCADE, null=True, blank=True)

class Avatar(models.Model):
    avatar=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)