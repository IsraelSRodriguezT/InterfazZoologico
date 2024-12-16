# Generated by Django 5.1.4 on 2024-12-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_cientifico', models.CharField(max_length=100)),
                ('peso', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]