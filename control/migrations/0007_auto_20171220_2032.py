# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_auto_20171220_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenador',
            name='link',
        ),
        migrations.AlterField(
            model_name='entrenador',
            name='imagen',
            field=models.ImageField(null=True, upload_to='entrenadores/', verbose_name='Imagen', blank=True),
        ),
    ]
