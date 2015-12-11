from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    county = models.CharField(max_length=255)
    sub_county = models.CharField(max_length=255)

    def __unicode__(self):
        return "Contact {0} {1} {2}".format(self.name, self.mobile_number, self.email)


class UserProfile(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    date_joined = models.DateTimeField(default=timezone.now)
    api_key = models.CharField(max_length=32)

    objects = UserManager()

    def __unicode__(self):
        return "UserProfile {0} {1}".format(self.first_name, self.email)
