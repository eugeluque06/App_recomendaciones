# Generated by Django 4.0.3 on 2022-07-06 16:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_peliculas', '0008_remove_critica_resenia_aprobada_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Actor', 'verbose_name_plural': 'Actores'},
        ),
        migrations.AlterModelOptions(
            name='critica',
            options={'verbose_name': 'Critica', 'verbose_name_plural': 'Criticas'},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'verbose_name': 'Director', 'verbose_name_plural': 'Directores'},
        ),
        migrations.AlterModelOptions(
            name='pelicula',
            options={'verbose_name': 'Pelicula', 'verbose_name_plural': 'Peliculas'},
        ),
        migrations.AlterField(
            model_name='critica',
            name='email_usuario',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='critica',
            name='estado_resenia',
            field=models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aprobada'), ('R', 'Rechazada')], default='P', max_length=9, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='critica',
            name='nombre_usuario',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='critica',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_peliculas.pelicula', verbose_name='Pelicula'),
        ),
        migrations.AlterField(
            model_name='critica',
            name='puntaje',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Puntaje'),
        ),
        migrations.AlterField(
            model_name='critica',
            name='resenia',
            field=models.TextField(blank=True, max_length=400, verbose_name='Reseña'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='actores',
            field=models.ManyToManyField(related_name='pelicula', to='App_peliculas.actor'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pelicula', to='App_peliculas.director'),
        ),
    ]