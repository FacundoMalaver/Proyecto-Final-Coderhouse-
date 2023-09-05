# Generated by Django 4.2.4 on 2023-09-04 21:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppMail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo_mensaje', models.CharField(max_length=1000)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('emisario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emisario', to=settings.AUTH_USER_MODEL)),
                ('recipiente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Mensaje',
        ),
    ]
