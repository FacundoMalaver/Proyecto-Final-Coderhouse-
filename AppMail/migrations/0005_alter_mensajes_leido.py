# Generated by Django 4.2.4 on 2023-09-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMail', '0004_mensajes_leido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='leido',
            field=models.CharField(default='No leido', max_length=10),
        ),
    ]
