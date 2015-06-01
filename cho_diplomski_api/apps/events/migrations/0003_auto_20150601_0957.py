# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventinvitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinvitation',
            name='event',
            field=models.ForeignKey(related_name='invitations', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='eventinvitation',
            name='status',
            field=model_utils.fields.StatusField(default=b'accepted', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
    ]
