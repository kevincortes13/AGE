# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20171216_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='content',
        ),
        migrations.AlterField(
            model_name='noticias',
            name='contenido',
            field=tinymce.models.HTMLField(verbose_name='Contenido'),
        ),
    ]
