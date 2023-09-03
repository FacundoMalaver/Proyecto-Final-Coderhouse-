from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Reseña)
admin.site.register(Avatar)
admin.site.register(Portada)
