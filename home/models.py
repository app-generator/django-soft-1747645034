# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Event(models.Model):

    #__Event_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    description = models.TextField(max_length=255, null=True, blank=True)
    registration = models.BooleanField()
    max_people = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    #__Event_FIELDS__END

    class Meta:
        verbose_name        = _("Event")
        verbose_name_plural = _("Event")


class Client(models.Model):

    #__Client_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")



#__MODELS__END
