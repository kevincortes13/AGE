# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20171216_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticias',
            old_name='HTML',
            new_name='content',
        ),
    ]
