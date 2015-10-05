# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_app', '0002_auto_20151003_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='shop',
            field=models.ForeignKey(null=True, to='expenses_app.Shop'),
        ),
    ]
