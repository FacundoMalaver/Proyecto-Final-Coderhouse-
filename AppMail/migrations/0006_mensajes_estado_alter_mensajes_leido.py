# Generated by Django 4.2.4 on 2023-09-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMail', '0005_alter_mensajes_leido'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='estado',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='leido',
            field=models.BooleanField(default=False),
        ),
    ]
