# Generated by Django 5.1.4 on 2024-12-16 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claseZoologico', '0008_direccion_guia_personallimpieza_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personallimpieza',
            options={'verbose_name': 'Personal de Limpieza', 'verbose_name_plural': 'Personales de Limpieza'},
        ),
        migrations.RemoveField(
            model_name='animal',
            name='tipo_alimento',
        ),
    ]
