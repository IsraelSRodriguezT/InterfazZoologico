# Generated by Django 5.1.4 on 2024-12-15 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claseZoologico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula:')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula:')),
                ('identificacion', models.CharField(max_length=7, unique=True, verbose_name='Identificacion:')),
                ('salario', models.FloatField()),
                ('zona', models.CharField(choices=[('NORTE', 'NORTE'), ('SUR', 'SUR'), ('ESTE', 'ESTE'), ('OESTE', 'OESTE')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula:')),
                ('identificacion', models.CharField(max_length=7, unique=True, verbose_name='Identificacion:')),
                ('salario', models.FloatField()),
                ('zona', models.CharField(choices=[('NORTE', 'NORTE'), ('SUR', 'SUR'), ('ESTE', 'ESTE'), ('OESTE', 'OESTE')], max_length=50, null=True)),
                ('especialidad', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animales:'},
        ),
        migrations.AddField(
            model_name='animal',
            name='estado',
            field=models.CharField(choices=[('NORMAL', 'NORMAL'), ('DESCANSANDO', 'DESCANSANDO'), ('ENFERMO', 'ENFERMO'), ('HERIDO', 'HERIDO'), ('ESTRESADO', 'ESTRESADO'), ('HAMBRIENTO', 'HAMBRIENTO'), (' COMIENDO', 'COMIENDO')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo_alimento',
            field=models.CharField(choices=[('CARNE', 'CARNE'), ('PESCADO', 'PESCADO'), ('HIERBA', 'HIERBA'), ('FRUTA', 'FRUTA')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo_cuerpo',
            field=models.CharField(choices=[('INVERTEBRADO', 'INVERTEBRADO'), ('VERTEBRADO', 'VERTEBRADO')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo_dieta',
            field=models.CharField(choices=[('CARNIVORO', 'CARNIVORO'), ('HERVIVORO', 'HERVIVORO'), ('OMNIVORO', 'OMNIVORO')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='zona',
            field=models.CharField(choices=[('NORTE', 'NORTE'), ('SUR', 'SUR'), ('ESTE', 'ESTE'), ('OESTE', 'OESTE')], max_length=50, null=True),
        ),
    ]
