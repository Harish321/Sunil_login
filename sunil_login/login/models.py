# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
class sunil(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
class check_login(models.Model):
    value = models.IntegerField(default=0)