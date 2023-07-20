# Generated by Django 4.0.3 on 2022-07-08 13:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_peliculas', '0010_alter_actor_biografia_alter_director_biografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critica',
            name='puntaje',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Puntaje'),
        ),
        migrations.AlterField(
            model_name='critica',
            name='resenia',
            field=models.TextField(blank=True, max_length=600, verbose_name='Reseña'),
        ),
    ]