# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect

#from multiupload.fields import MultiFileField
from .models import Report
#from .models import Report_Folder


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password', 'is_superuser']

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username", max_length = 100)
    password = forms.CharField(label = "Password", max_length = 100, widget = forms.PasswordInput)

class LOUForm(forms.ModelForm):
    is_activated = forms.BooleanField()
    class Meta:
        model = User
        fields = {'is_activated'}


class ReportForm(forms.ModelForm):
     class Meta:
        model = Report
        fields = ['short','detailed','file1','file2','file3','file4','file5','visibility','encrypt']
        #widgets = {'visibility': RadioSelect(),}

#    files = MultiFileField(min_num=0, max_num=3, max_file_size=1024*1024*5)

#    def save(self, commit=True):
#        instance = super(ReportForm, self).save(commit)
#        for each in self.cleaned_data['files']:
#            Attachment.objects.create(file=each, report=instance)

#        return instance

# want to use pm_write(sender, recipient, subject, body='', skip_notification=False,
#         auto_archive=False, auto_delete=False, auto_moderators=None):

from postman.models import Message

class BroadcastForm(forms.Form):
    subject = forms.CharField(label = "Subject", max_length = 100)
    body = forms.CharField(label = "Message",widget=forms.Textarea)
    encrypted = forms.BooleanField(label="Encrypt: ", required=False)
    enc_key = forms.CharField(label = "Encryption Key: ", max_length = 100, required=False)

    class Meta:
        model = Message
        fields = ['sender',
        'recipient' ,
        'subject' ,
        'body',
        'encrypted',
        'enc_key']


class MessageForm(forms.Form):

    recipient = forms.CharField(label = "Recipient", max_length = 100)
    subject = forms.CharField(label = "Subject", max_length = 100)
    body = forms.CharField(label = "Message",widget=forms.Textarea)
    encrypted = forms.BooleanField(label="Encrypt ", required=False)
    enc_key = forms.CharField(label = "Encryption Key ", max_length = 100, required=False)

    class Meta:
        model = Message
        fields = ['sender',
        'recipient' ,
        'subject' ,
        'body',
        'encrypted',
        'enc_key']

'''
class Report_FolderForm(forms.ModelForm):

    class Meta:
        model = Report_Folder
        fields = ['folder_name', 'files', 'visibility']
'''
