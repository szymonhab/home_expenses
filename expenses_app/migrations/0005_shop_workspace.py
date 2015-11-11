# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_app', '0004_workspace_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='workspace',
            field=models.ForeignKey(default=1, to='expenses_app.Workspace'),
            preserve_default=False,
        ),
    ]
