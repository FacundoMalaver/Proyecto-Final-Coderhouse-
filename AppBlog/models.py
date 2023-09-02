from django.db import models
import datetime

# Create your models here.

class Reseña(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField(default=datetime.date.today)
    autor=models.CharField(max_length=20, default='Autor Reseña')
    cuerpo=models.CharField(max_length=1000, default='Cuerpo Reseña')
    def __str__(self):
        return f'{self.titulo} - {self.fecha} - {self.autor}'
