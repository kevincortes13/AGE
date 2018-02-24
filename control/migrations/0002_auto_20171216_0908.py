# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='HTML',
            field=tinymce.models.HTMLField(verbose_name='Content', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='fecha_creado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
