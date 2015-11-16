# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
