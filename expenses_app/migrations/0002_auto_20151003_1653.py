# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=127),
        ),
    ]
