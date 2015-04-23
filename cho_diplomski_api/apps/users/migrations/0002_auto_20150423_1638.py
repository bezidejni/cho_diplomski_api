# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=model_utils.fields.StatusField(no_check_for_status=True, max_length=100, default='user', choices=[(0, 'dummy')]),
        ),
    ]
