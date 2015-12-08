# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
#from django.utils.translation import ugettext_lazy as _

class Folder(models.Model):
    username = models.CharField(max_length=200, default='null')
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Report(models.Model):
    #username that uploaded file
    username = models.CharField(max_length=200, default='null')
    #timestamp
    timestamp = models.DateTimeField(default=timezone.now)
    #short description
    short = models.CharField(max_length=200)
    #detailed description22
    detailed = models.TextField(default='')
    #one or more files
    file1 = models.FileField(upload_to='attachments',blank=True, null=True)
    file2 = models.FileField(upload_to='attachments',blank=True, null=True)
    file3 = models.FileField(upload_to='attachments',blank=True, null=True)
    file4 = models.FileField(upload_to='attachments',blank=True, null=True)
    file5 = models.FileField(upload_to='attachments',blank=True, null=True)
    file_list = [file1,file2,file3,file4,file5]
    #private/public
    P_CHOICES = (
        (u'private', u'private'),
        (u'public', u'public'),
    )
    visibility = models.CharField(max_length=7, choices=P_CHOICES, default='private')
    folder = models.ForeignKey(Folder, null=True)
    encrypt = models.BooleanField(default=False)
    group = models.ManyToManyField(Group, null=True)
    def __str__(self):
        return self.short


#class Attachment(models.Model):
#    report = models.ForeignKey(Report, verbose_name=_('Report'), related_name='attachment_set', blank=True, null=True)
#    file = models.FileField(_('Attachment'), upload_to='attachments', blank=True, null=True)
#class File(models.Model):
 #   file = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)
  #  property = models.ForeignKey('Report', related_name="files")
#    def __str__(self):
#        return self.file.name
    #class Meta:
    #    ordering = ('user',)
#class Permision(models.Model):
#    name = models.CharField(max_length=50, default="null")
#    content_type =

#class Group(models.Model):
 #    name = models.CharField(max_length=80, default="null")
  #   permissions = models.ManyToManyField(Permission)

class User(models.Model):
     first_name = models.CharField(max_length=200, default="null")
     last_name = models.CharField(max_length=200, default="null")
     username = models.CharField(max_length=200, default="null")
     password = models.CharField(max_length=200, default="null")
     is_superuser = models.BooleanField(default="false")

