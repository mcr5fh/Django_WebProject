# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from myapplication.forms import UserForm, LOUForm
from django.views.generic.edit import FormView
from myapplication.forms import UserForm, MessageForm, BroadcastForm
from myapplication.models import Report

from myapplication.models import Folder


#from myapplication.models import Attachment

#from myapplication.forms import Report_FolderForm
#from myapplication.models import Report_Folder

from myapplication.forms import ReportForm
from django.utils import timezone
from myapplication.forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import os
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Util import Counter

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def list_of_users(request):
    if request.user.is_superuser:
        lou_form = LOUForm(data=request.POST)
        list = User.objects.all()
        return render(request, 'list_of_users_sm.html', {'lou_form':lou_form,'list': list})
    else:
        return render(request,'list_of_users.html')


@login_required
def report_new(request):
    #logger.error("User in request: " + request.user.username)
    # Handle file upload
    if request.method == 'POST':
        logger.error("User in request: " + request.user.username)
        form = ReportForm(request.POST, request.FILES)#, {'user': request.user.username})

        if form.is_valid():

            #newReport = form.save(commit=False)
            #newReport.timestamp = timezone.now()

            #if request.FILES['file']:
            #   newReport.file = request.FILES['file']
            #newReport.save()

            #form.Meta.fields = request.user.username
            newReport = form.save(commit=False)
            newReport.username = request.user.username

            newReport.save()

            #for afile in request.FILES.getlist('files'):
                #add file to model


            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapplication.views.manage'))
    else:
        form = ReportForm() # A empty, unbound form
       # fileForm = FileForm()
    return render(request, 'report.html', {'form': form})


#test this more. Admin must be able to see all reports
@login_required
def list(request):

    # Load documents for the list page
    #attachments = Attachment.objects.all()

    if request.user.is_superuser:
        reports = Report.objects.all()
    else:
       reports = Report.objects.filter(Q(username=request.user.username) | Q(visibility="public"))

    #TODO: Add visibility to folders
    #folders = Report_Folder.objects.filter(Q(user=request.user.username))
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'reports': reports},
        context_instance=RequestContext(request)
    )

'''
@login_required
def report_folder_new(request):

    folder_form = Report_FolderForm()

    return render(request, 'report_folder.html', {'folder_form': folder_form})
'''


@login_required
def delete(request):
    if request.method != 'POST':
        logger.error("METHOD NOT POST")
        #raise HTTP404

    reportId = request.POST.get('report', None)
    reportToDel = get_object_or_404(Report, pk = reportId)
    #for attachment in reportToDel.attachment_set.all():
    #    attachment.file.delete()
    #    attachment.delete()
    if reportToDel.file1:
        reportToDel.file1.delete()
    if reportToDel.file2:
        reportToDel.file2.delete()
    if reportToDel.file3:
        reportToDel.file3.delete()
    if reportToDel.file4:
        reportToDel.file4.delete()
    if reportToDel.file5:
        reportToDel.file5.delete()
    reportToDel.delete()

    return HttpResponseRedirect(reverse('myapplication.views.manage'))

@login_required
def report_edit(request, pk):
    report = Report.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.timestamp = timezone.now()
            #for attachment in report.attachment_set.all():
            #    attachment.file.save()
            #    attachment.save()
            report.save()
            #form.save()
            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapplication.views.manage'))
    else:
        form = ReportForm(instance=report)
    return render(request, 'report_edit.html', {'form': form, 'report': report})

@login_required
def manage(request):
    if request.user.is_superuser:
        reports = Report.objects.all()
    else:
        reports = Report.objects.filter(Q(username=request.user.username))
    folders = Folder.objects.filter(Q(username=request.user.username))


    # Render manage page with user reports and folders
    return render_to_response(
        'manage.html',
        {'reports': reports, 'folders': folders},
        context_instance=RequestContext(request)
    )

@login_required
def folder_new(request):
    #create new folder
    if request.method == 'POST':
        fname = request.POST.get("name", "")
        f = Folder(name=fname)
        f.username = request.user.username
        f.save()
    return HttpResponseRedirect(reverse('myapplication.views.manage'))

@login_required
def folder_delete(request):
    if request.method != 'POST':
        logger.log("METHOD NOT POST")
        #raise HTTP404

    folderPk = request.POST.get('folder', None)
    folderToDel = get_object_or_404(Folder, pk = folderPk)
    for reportToDel in folderToDel.report_set.all():
        folderToDel.report_set.remove(reportToDel);
        '''
        if reportToDel.file1:
            reportToDel.file1.delete()
        if reportToDel.file2:
            reportToDel.file2.delete()
        if reportToDel.file3:
            reportToDel.file3.delete()
        if reportToDel.file4:
            reportToDel.file4.delete()
        if reportToDel.file5:
            reportToDel.file5.delete()
        reportToDel.delete()
        '''
    folderToDel.delete()

    return HttpResponseRedirect(reverse('myapplication.views.manage'))

@login_required
def move_report(request):
    #create new folder
    if request.method == 'POST':
        reportPk = request.POST.get("reportpk", "")
        folderPk = request.POST.get("folderpk", "")
        r = Report.objects.get(pk=reportPk)
        f = Folder.objects.get(pk=folderPk)
        f.report_set.add(r)
        f.save()
        #f.save()
        #r.save()
    return HttpResponseRedirect(reverse('myapplication.views.manage'))

@login_required
def remove_report(request):

    if request.method == 'POST':
        reportPk = request.POST.get("report", "")
        folderPk = request.POST.get("folder", "")
        r = Report.objects.get(pk=reportPk)
        f = Folder.objects.get(pk=folderPk)
        f.report_set.remove(r)
        f.save()
        #f.save()
        #r.save()
    return HttpResponseRedirect(reverse('myapplication.views.manage'))

#NOTE: if user already exists then it jsut resets
def register(request):
    context = RequestContext(request)
    #a boolean value for telling the template whether the registration was successful. Set to False originally, code changes to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data
    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        
        
        #validation checking...
        if user_form.is_valid():
            
            user = user_form.save()
            
            user.set_password(user.password)
            
            user.save()

#profile = profile_form.save(commit=False)

#           profile.user = user

        #save the UserProfile model instance/update variable to tell the template registration was successful

#profile.save()

            registered = True


    else:
        user_form = UserForm()
#profile_form = UserProfileForm()

    return render_to_response('register.html', {'user_form': user_form,'registered': registered}, context)


def login_view(request):
    context = RequestContext(request)
    logged_in = False
    invalid_login = False

    if request.method == 'POST':

         #check to see if the post came from the logout in the reports page
        if 'logout' in request.POST:
            logout(request)
            logger.error('Logging out')
            login_form = LoginForm()
            return render(request, 'login.html', {'login_form': login_form, 'invalid_log': invalid_login})

        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    logged_in = True
                    logger.error("User: " + user.username)
                    # Return to reports page
                    return render_to_response('index.html', {'login_form': login_form,'logged_in': logged_in, 'user': user}, context)
            else:
                logger.error('invalid login error message')
                logged_in = False
                invalid_login = True
                login_form = LoginForm()
                return render(request, "login.html", {'login_form': login_form, 'invalid_log': invalid_login, 'logged_in': logged_in})


                    
    else:
        if request.user.is_authenticated():
            logged_in = True
        login_form = LoginForm()
    
    return render_to_response('login.html', {'login_form': login_form,'logged_in': logged_in}, context)

from postman.api import pm_write, pm_broadcast

def send_broadcast(request):
    if request.method == 'POST':
        form = BroadcastForm(request.POST)

        #validation checking...
        if form.is_valid():
            sender = request.user

            subject = request.POST['subject']
            text = request.POST['body']
            encrypted = request.POST.get('encrypted', False)
            enc_key = request.POST['enc_key']
            if enc_key == "":
                enc_key = "N/A"
            else:
                #encrypt
                hash_pw = SHA256.new(str.encode(enc_key))
                sym_key = hash_pw.digest()
                if len(sym_key) >= 16:
                    if(len(sym_key) < 24 ):
                        sym_key = sym_key[0:16]
                    elif len(sym_key) < 32:
                        sym_key = sym_key[0:24]
                    elif len(sym_key) > 32:
                        sym_key = sym_key[0:32]
                encryption_suite = AES.new(sym_key, AES.MODE_CTR, b"", Counter.new(128))
                text = encryption_suite.encrypt(text)


            pm_broadcast(sender,"", subject, encrypted, body=text)
            return render(request, 'postman/inbox.html', )
        else:
            return render(request, 'broadcast.html', {'message_form': form })


    else:
        form = BroadcastForm()
        return render(request, 'broadcast.html', {'message_form': form })


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        #validation checking...
        if form.is_valid():
            sender = request.user
            recipient_name = request.POST['recipient']
            try:
                recipient = User.objects.get(username=recipient_name)
            except  User.DoesNotExist:
                error = "User does not exist.  Please enter a valid username"
                return render(request, 'new_message.html', {'message_form': form , "error": error})

            subject = request.POST['subject']
            text = request.POST['body']
            encrypted = request.POST.get('encrypted', False)
            enc_key = request.POST['enc_key']
            if enc_key == "":
                enc_key = "N/A"
            else:
                #encrypt
                hash_pw = SHA256.new(str.encode(enc_key))
                sym_key = hash_pw.digest()
                if len(sym_key) >= 16:
                    if(len(sym_key) < 24 ):
                        sym_key = sym_key[0:16]
                    elif len(sym_key) < 32:
                        sym_key = sym_key[0:24]
                    elif len(sym_key) > 32:
                        sym_key = sym_key[0:32]
                encryption_suite = AES.new(sym_key, AES.MODE_CTR, b"", Counter.new(128))
                text = encryption_suite.encrypt(text)


            pm_write(sender,recipient,subject, encrypted, body=text)
            return render(request, 'postman/inbox.html', )
        else:
            return render(request, 'new_message.html', {'message_form': form })


    else:
        form = MessageForm()
        return render(request, 'new_message.html', {'message_form': form })

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    badDate = False

    if ('q' in request.GET) and request.GET['q'].strip():
        search_fields = []

        if ('uploadedby' in request.GET):
            search_fields.append('username')
        if ('short' in request.GET):
            search_fields.append('short')
        if ('description' in request.GET):
            search_fields.append('detailed')
        if ('files' in request.GET):
            search_fields.append('file1')
            search_fields.append('file2')
            search_fields.append('file3')
            search_fields.append('file4')
            search_fields.append('file5')

        query_string = request.GET['q']

        if len(search_fields) != 0:
            entry_query = get_query(query_string, search_fields)
            if request.user.is_superuser:
                found_entries = Report.objects.all()
            else:
                found_entries = Report.objects.filter(Q(username=request.user.username) | Q(visibility="public")).filter(entry_query).order_by('timestamp')

        else:
            found_entries = None

        begin = request.GET['begin']
        end = request.GET['end']

        beginMatch = re.match('\d{4}-\d{2}-\d{2}', begin)
        endMatch = re.match('\d{4}-\d{2}-\d{2}', end)
        if beginMatch and endMatch:
            found_entries = found_entries.filter(timestamp__range=[begin,end])
            badDate = False
        else:
            badDate = True

        visibilityGet = request.GET['visibility']
        if (visibilityGet == "all"):
            pass
        else:
            found_entries = found_entries.filter(visibility=visibilityGet)
    else:
        if request.user.is_superuser:
            found_entries = Report.objects.all()
        else:
            found_entries = Report.objects.filter(Q(username=request.user.username) | Q(visibility="public")).order_by('timestamp')
        begin = request.GET['begin']
        end = request.GET['end']

        beginMatch = re.match('\d{4}-\d{2}-\d{2}', begin)
        endMatch = re.match('\d{4}-\d{2}-\d{2}', end)
        if beginMatch and endMatch:
            found_entries = found_entries.filter(timestamp__range=[begin,end])
            badDate = False
        else:
            badDate = True

        visibilityGet = request.GET['visibility']
        if (visibilityGet == "all"):
            pass
        else:
            found_entries = found_entries.filter(visibility=visibilityGet)


    return render_to_response('search.html',
                          { 'query_string': query_string, 'found_entries': found_entries, 'bad_date': badDate },
                          context_instance=RequestContext(request))

