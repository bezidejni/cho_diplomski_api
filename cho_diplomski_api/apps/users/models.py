from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField


class User(AbstractUser):
    ROLES = Choices('admin', 'user')
    phone_number = models.CharField(max_length=15)
    role = StatusField(choices_name='ROLES', default=ROLES.user)
