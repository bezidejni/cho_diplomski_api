# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('application_deadline', models.DateTimeField()),
            ],
        ),
    ]
