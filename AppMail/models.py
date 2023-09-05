from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Mensajes(models.Model):
    emisario=models.ForeignKey(User, on_delete=models.SET_NULL, related_name="emisario", null=True)
    recipiente=models.ForeignKey(User, on_delete=models.SET_NULL, related_name="receiver", null=True)
    asunto=models.CharField(max_length=100, default='')
    cuerpo_mensaje=models.CharField(max_length=1000)
    fecha=models.DateField(default=datetime.date.today)
