# Generated by Django 5.1.4 on 2024-12-15 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claseZoologico', '0002_cliente_cuidador_veterinario_alter_animal_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animales'},
        ),
    ]
