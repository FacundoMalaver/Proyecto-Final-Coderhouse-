from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Mensaje(models.Model):
    sender=models.ForeignKey(User, on_delete=models.SET_NULL, related_name="sender", null=True)
    reciever=models.ForeignKey(User, on_delete=models.SET_NULL, related_name="receiver", null=True)
    cuerpo_mensaje=models.CharField(max_length=1000)
    fecha=models.DateField(default=datetime.date.today)