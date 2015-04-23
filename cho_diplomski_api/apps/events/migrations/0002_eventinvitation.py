# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], no_check_for_status=True, max_length=100, default='pending')),
                ('event', models.ForeignKey(to='events.Event', related_name='users')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='events')),
            ],
        ),
    ]
