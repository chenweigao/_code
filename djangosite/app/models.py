# -*- coding: utf-8 -*-
from django.db import models
from __future__ import models

KIND_CHOICES = (
    ('Python')
)
# Create your models here.
class Moment (models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length = 20)
    kind = models.CharField(max_length=20)
