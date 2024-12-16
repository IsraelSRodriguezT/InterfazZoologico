# Generated by Django 5.1.4 on 2024-12-16 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claseZoologico', '0007_alter_jaula_esta_limpio_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle_principal', models.CharField(max_length=100, verbose_name='Calle principal')),
                ('calle_secundaria', models.CharField(max_length=100, verbose_name='Calle secundaria')),
                ('referencia', models.CharField(max_length=100, verbose_name='Referencia')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula:')),
                ('identificacion', models.CharField(editable=False, max_length=7, unique=True)),
                ('salario', models.FloatField()),
                ('zona', models.CharField(choices=[('NORTE', 'NORTE'), ('SUR', 'SUR'), ('ESTE', 'ESTE'), ('OESTE', 'OESTE')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalLimpieza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula:')),
                ('identificacion', models.CharField(editable=False, max_length=7, unique=True)),
                ('salario', models.FloatField()),
                ('zona', models.CharField(choices=[('NORTE', 'NORTE'), ('SUR', 'SUR'), ('ESTE', 'ESTE'), ('OESTE', 'OESTE')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='cuidador',
            options={'verbose_name': 'Cuidador', 'verbose_name_plural': 'Cuidadores'},
        ),
        migrations.RemoveField(
            model_name='compra',
            name='boleto',
        ),
        migrations.RemoveField(
            model_name='jaula',
            name='animal',
        ),
        migrations.AddField(
            model_name='animal',
            name='cuidador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animales', to='claseZoologico.cuidador'),
        ),
        migrations.AddField(
            model_name='animal',
            name='jaula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animales', to='claseZoologico.jaula'),
        ),
        migrations.AddField(
            model_name='animal',
            name='veterinario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animales', to='claseZoologico.veterinario'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='compra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boletos', to='claseZoologico.compra'),
        ),
        migrations.AlterField(
            model_name='boleto',
            name='cliente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boleto', to='claseZoologico.cliente'),
        ),
        migrations.AlterField(
            model_name='jaula',
            name='esta_limpio',
            field=models.BooleanField(null=True, verbose_name='Esta limpio'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='guia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='claseZoologico.guia'),
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField()),
                ('fecha', models.DateField(auto_now=True)),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historial_medico_list', to='claseZoologico.animal')),
            ],
        ),
        migrations.AddField(
            model_name='jaula',
            name='personal_limpieza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jaulas', to='claseZoologico.personallimpieza', verbose_name='Personal limpieza:'),
        ),
        migrations.CreateModel(
            name='Zoologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=10, unique=True)),
                ('direccion', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='claseZoologico.direccion')),
            ],
            options={
                'verbose_name': 'Zoológico',
                'verbose_name_plural': 'Zoológicos',
            },
        ),
        migrations.AddField(
            model_name='personallimpieza',
            name='zoologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_limpieza_list', to='claseZoologico.zoologico'),
        ),
        migrations.AddField(
            model_name='guia',
            name='zoologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guias', to='claseZoologico.zoologico'),
        ),
        migrations.AddField(
            model_name='animal',
            name='zoologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animales', to='claseZoologico.zoologico'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='zoologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='claseZoologico.zoologico'),
        ),
        migrations.AddField(
            model_name='cuidador',
            name='zoologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuidadores', to='claseZoologico.zoologico'),
        ),
        migrations.AddField(
            model_name='veterinario',
            name='zoologico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='veterinarios', to='claseZoologico.zoologico'),
        ),
    ]