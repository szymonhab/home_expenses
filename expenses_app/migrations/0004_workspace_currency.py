# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_app', '0003_auto_20151005_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='currency',
            field=models.CharField(default='zł', max_length=15),
            preserve_default=False,
        ),
    ]
