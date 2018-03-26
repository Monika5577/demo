# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = 'profile'