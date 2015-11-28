# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Report(models.Model):
    #timestamp
    timestamp = models.DateTimeField(default=timezone.now)
    #short description
    short = models.CharField(max_length=200)
    #detailed description
    detailed = models.TextField()
    #one or more files
    file = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True)
    #private/public