from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    application_deadline = models.DateTimeField()
