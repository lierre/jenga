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
    creator = models.ManyToManyField(User)

    def __unicode__(self):
        return "Contact {0} {1} {2}".format(self.name, self.mobile_number, self.email)


class Organization(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(default=timezone.now)
    member = models.ManyToManyField(User)

    def __unicode__(self):
        return "Organization {0}".format(self.name)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    date_joined = models.DateTimeField(default=timezone.now)
    api_key = models.CharField(max_length=32)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'email'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        return super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_display_name(self):
        return self.username or self.email

    class Meta:
        verbose_name_plural = 'users'

    def __unicode__(self):
        return "UserProfile {0} {1}".format(self.first_name, self.email)
