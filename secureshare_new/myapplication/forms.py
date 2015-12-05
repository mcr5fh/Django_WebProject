# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'is_superuser']
        
from .models import Report


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username", max_length = 100)
    password = forms.CharField(label = "Password", max_length = 100, widget = forms.PasswordInput)
from .models import Report


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['short','detailed','file','visibility']
        #widgets = {'visibility': RadioSelect(),}


class LOUForm(forms.ModelForm):
    is_activated = forms.BooleanField()
    class Meta:
        model = User
        fields = {'is_activated'}




