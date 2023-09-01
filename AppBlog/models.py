from django.db import models

# Create your models here.

class Reseña(models.Model):
    titulo=models.CharField(max_length=20)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField
    autor=models.CharField
