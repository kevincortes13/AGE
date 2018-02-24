# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_auto_20171216_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id_e', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(verbose_name='Nacionalidad', max_length=40)),
                ('division', models.CharField(max_length=7, choices=[('primera', '1era Division'), ('segunda', '2da Division'), ('tercera', '3ra Division')])),
                ('imagen', models.ImageField(verbose_name='Imagen', null=True, upload_to='jugadores/', blank=True)),
                ('link', models.URLField(default='#')),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id_e'],
            },
        ),
        migrations.DeleteModel(
            name='MiEquipo',
        ),
    ]
