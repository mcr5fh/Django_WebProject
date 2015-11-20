# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'is_superuser']
        
from .models import Report

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('short','detailed','file',)


