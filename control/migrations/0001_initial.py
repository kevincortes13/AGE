# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre_club', models.CharField(verbose_name='Club', max_length=40)),
                ('logo_club', models.ImageField(null=True, upload_to='club/', verbose_name='Logo del Club', blank=True)),
            ],
            options={
                'ordering': ['nombre_club'],
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id_j', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(verbose_name='Nacionalidad', max_length=40)),
                ('posicion', models.CharField(max_length=15, choices=[('porteros', 'Portero'), ('defensas', 'Defensa'), ('centrocampistas', 'CentroCampista'), ('delanteros', 'Delantero')])),
                ('division', models.CharField(max_length=7, choices=[('primera', '1era Division'), ('segunda', '2da Division'), ('tercera', '3ra Division')])),
                ('imagen', models.ImageField(null=True, upload_to='jugadores/', verbose_name='Imagen', blank=True)),
                ('link', models.URLField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('club', models.ForeignKey(blank=True, to='control.Club', related_name='c', null=True)),
            ],
            options={
                'ordering': ['-id_j'],
            },
        ),
        migrations.CreateModel(
            name='MiEquipo',
            fields=[
                ('tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id_n', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('enlace', models.SlugField(unique=True)),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(verbose_name='Fecha (Y-M-D)')),
                ('imagen_noticia', models.ImageField(null=True, upload_to='noticias/', verbose_name='Imagen de la Noticia', blank=True)),
                ('delegacion', multiselectfield.db.fields.MultiSelectField(max_length=41, choices=[('occidental', 'GrupoElite Occidental'), ('central', 'GrupoElite Central'), ('oriental', 'GrupoElite Oriental'), ('internacional', 'GrupoElite Internacional')])),
                ('fecha_creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('futbolistas', models.ManyToManyField(to='control.Jugador', null=True, blank=True)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
    ]
