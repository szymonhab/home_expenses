# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('bill_date', models.DateField()),
                ('add_datetime', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='BillRow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('label', models.CharField(max_length=127)),
                ('bill', models.ForeignKey(to='expenses_app.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('surname', models.TextField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='workspace',
            field=models.ForeignKey(to='expenses_app.Workspace'),
        ),
        migrations.AddField(
            model_name='category',
            name='workspace',
            field=models.ForeignKey(to='expenses_app.Workspace'),
        ),
        migrations.AddField(
            model_name='billrow',
            name='category',
            field=models.ForeignKey(to='expenses_app.Category'),
        ),
        migrations.AddField(
            model_name='bill',
            name='person',
            field=models.ForeignKey(to='expenses_app.Person'),
        ),
        migrations.AddField(
            model_name='bill',
            name='workspace',
            field=models.ForeignKey(to='expenses_app.Workspace'),
        ),
    ]
