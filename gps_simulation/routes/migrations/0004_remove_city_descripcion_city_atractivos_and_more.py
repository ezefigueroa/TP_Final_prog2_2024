# Generated by Django 5.1.1 on 2024-11-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_city_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='city',
            name='atractivos',
            field=models.TextField(default='Sin descripción'),
        ),
        migrations.AddField(
            model_name='city',
            name='descubre_el_lugar',
            field=models.TextField(default='Sin descripción'),
        ),
    ]