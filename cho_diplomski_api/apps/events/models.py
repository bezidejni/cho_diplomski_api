from django.conf import settings
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField


class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    application_deadline = models.DateTimeField()

    def __unicode__(self):
        return self.name


class EventInvitation(models.Model):
    STATUS = Choices('accepted', 'rejected')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events')
    event = models.ForeignKey(Event, related_name='invitations')
    status = StatusField(default=STATUS.accepted)
