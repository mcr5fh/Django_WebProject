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
from django.contrib.auth.models import User, Group
from myapplication.forms import UserForm, LOUForm, DeactivateForm, SuperUserForm,DisableSuperUserForm, CreateGroupForm, AddUserToGroupForm
from django.views.generic.edit import FormView
from myapplication.forms import UserForm, MessageForm, BroadcastForm
from myapplication.models import Report

from myapplication.models import Folder


# from myapplication.models import Attachment

# from myapplication.forms import Report_FolderForm
# from myapplication.models import Report_Folder

from myapplication.forms import ReportForm
from django.utils import timezone
from myapplication.forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
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
def deactivate(request):
    if request.user.is_superuser:
        deactivated = False
        if request.method == 'POST':
            deactivate_form = DeactivateForm(data=request.POST)
            if deactivate_form.is_valid():
                deactivate_name = request.POST['user_to_deactivate']
                user = User.objects.get(username=deactivate_name)
                user.is_active = False
                user.save()
                deactivated = True
            else:
                deactivate_form = DeactivateForm()
        else:
            deactivate_form = DeactivateForm()
        return render(request,'deactivate.html',{'deactivate_form': deactivate_form, 'deactivated':deactivated})
    else:
        return render(request,'list_of_users.html')


@login_required
def make_super_user(request):
    if request.user.is_superuser:
        made_super_user = False
        if request.method == 'POST':
            super_user_form = SuperUserForm(data=request.POST)
            if super_user_form.is_valid():
                superuser_name = request.POST['super_user']
                user = User.objects.get(username=superuser_name)
                user.is_superuser = True
                user.save()
                made_super_user
            else:
                super_user_form = SuperUserForm()
        else:
            super_user_form = SuperUserForm()
        return render(request, 'make_super_user.html', {'super_user_form':super_user_form, 'made_super_user':made_super_user})
    else:
        return render(request,'list_of_users.html')


@login_required
def disable_super_user(request):
    if request.user.is_superuser:
        disabled_super_user = False
        if request.method == 'POST':
            disable_super_user_form = DisableSuperUserForm(data=request.POST)
            if disable_super_user_form.is_valid():
                superuser_name = request.POST['disable_super_user']
                user = User.objects.get(username=superuser_name)
                user.is_superuser = False
                user.save()
                disabled_super_user = True
            else:
                disable_super_user_form = DisableSuperUserForm()
        else:
            disable_super_user_form = DisableSuperUserForm()
        return render(request, 'disable_super_user.html', {'disable_super_user_form':disable_super_user_form, 'disabled_super_user':disabled_super_user})
    else:
        return render(request,'list_of_users.html')



@login_required
def group(request):
    users = User.objects.all()
    # get groups where user is in the group
    groups = []
    for g in request.user.groups.all():
        groups.append(g)
    return render(request, 'group.html', {'users': users, 'groups': groups})


@login_required
def group_new(request):
    # create new folder
    if request.method == 'POST':
        gname = request.POST.get("name", "")
        g = Group(name=gname)
        g.save()
        u = request.user
        u.groups.add(g)
        u.save()
    return HttpResponseRedirect(reverse('myapplication.views.group'))


@login_required
def group_delete(request):
    if request.method != 'POST':
        logger.log("METHOD NOT POST")
        # raise HTTP404

    groupPk = request.POST.get('group', None)
    groupToDel = get_object_or_404(Group, pk=groupPk)
    for userToDel in groupToDel.user_set.all():
        groupToDel.user_set.remove(userToDel);
        userToDel.save()
        groupToDel.save()

    groupToDel.delete()

    return HttpResponseRedirect(reverse('myapplication.views.group'))


def move_user(request):
    if request.method == 'POST':
        userPk = request.POST.get("userpk", "")
        groupPk = request.POST.get("grouppk", "")
        u = User.objects.get(pk=userPk)
        g = Group.objects.get(pk=groupPk)
        g.user_set.add(u)
        g.save()
    '''
    content_type = ContentType.objects.get(app_label='myapplication', model='Report')
    #permission = Permission.objects.create(codename='can_view', name='Can view Reports',
                                           content_type=content_type)
    #user = User.objects.get(username=username)
    #group = Group.objects.get(name=name)
    #group.permissions.add(permission)
    #user.groups.add(group)
    '''
    return HttpResponseRedirect(reverse('myapplication.views.group'))


@login_required
def remove_user(request):
    if request.method == 'POST':
        userPk = request.POST.get("user", "")
        groupPk = request.POST.get("group", "")
        u = User.objects.get(pk=userPk)
        g = Group.objects.get(pk=groupPk)
        g.user_set.remove(u)
        g.save()
        u.save()
        # f.save()
        # r.save()
    return HttpResponseRedirect(reverse('myapplication.views.group'))


@login_required
def list_of_users(request):
    if request.user.is_superuser:
        activated = False
        if request.method == 'POST':
            lou_form = LOUForm(data=request.POST)
            if lou_form.is_valid():
                activate_name = request.POST['user_to_activate']
                user = User.objects.get(username=activate_name)
                user.is_active = True
                user.save()
                activated = True
            else:
                lou_form = LOUForm()
        else:
            lou_form = LOUForm()
        return render(request, 'list_of_users_sm.html', {'lou_form':lou_form, 'activated':activated})
    else:
        return render(request, 'list_of_users.html')



@login_required
def edit_groups(request):
    if request.user.is_superuser:
        return render(request,'edit_groups.html')
    else:
        return render(request, 'list_of_users.html')


@login_required
def create_group(request):
    created = False
    if request.method == 'POST':
        new_group_form = CreateGroupForm(data = request.POST)
        if new_group_form.is_valid():
            group_name = request.POST['group_form']
            newgroup = Group.objects.create(name=group_name)
            created = True
    else:
        new_group_form = CreateGroupForm()

    return render(request, 'create_group.html', {'new_group_form':new_group_form, 'created':created})



@login_required
def add_to_group(request):
    added = False
    if request.method == 'POST':
        add_user_form = AddUserToGroupForm(data = request.POST)
        if add_user_form.is_valid:
            user_name = request.POST['add_user']
            add_to = request.POST['add_to_group']
            user = User.objects.get(username = user_name)
            g = Group.objects.get(name=add_to)
            #g.user_set.add(user_name)
            user.groups.add(g)
            added = True
    else:
        add_user_form = AddUserToGroupForm()
    return render(request, 'add_to_group.html', {'add_user_form':add_user_form, 'added':added})

@login_required
def report_new(request):
    # logger.error("User in request: " + request.user.username)
    # Handle file upload
    if request.method == 'POST':
        logger.error("User in request: " + request.user.username)
        form = ReportForm(request.POST, request.FILES)  # , {'user': request.user.username})

        if form.is_valid():
            # newReport = form.save(commit=False)
            # newReport.timestamp = timezone.now()

            # if request.FILES['file']:
            #   newReport.file = request.FILES['file']
            # newReport.save()

            # form.Meta.fields = request.user.username
            newReport = form.save(commit=False)
            newReport.username = request.user.username
            newReport.save()
            for g in request.user.groups.all():
                newReport.group.add(g)

            # for afile in request.FILES.getlist('files'):
            # add file to model


            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapplication.views.manage'))
    else:
        form = ReportForm()  # A empty, unbound form
        # fileForm = FileForm()
    return render(request, 'report.html', {'form': form})


# test this more. Admin must be able to see all reports
@login_required
def list(request):
    # Load documents for the list page
    # attachments = Attachment.objects.all()

    if request.user.is_superuser:
        reports = Report.objects.all()
    else:
        '''
        #list all reports that you created, and are public to you
        #also list all reports that you have been given access to:
        #All the groups you are in: get all the users in those groups: get their private reports
       group_list = request.user.group.values_list('')
       '''
        # query_string = "Q(username=request.user.username) | Q(visibility='public')"
        query = Q(username=request.user.username) | Q(visibility='public')
        for g in request.user.groups.all():
            print(str(g))
            query.add(Q(group=g), Q.OR)
        reports = Report.objects.filter(query)

        # When we add a user to a group, add the group to all the user's reports.group attribute
        # When we delete a user froma group, delete the group from all the user's reports.group attribute

        # trying to get all the reports associated with the groups you are in

    '''
      users = g.user_set.all()
      for user in users:
          #append user to unique users array

  reports = reports.filter(Q(group=))
  '''

    # TODO: Add visibility to folders
    # folders = Report_Folder.objects.filter(Q(user=request.user.username))
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
        # raise HTTP404

    reportId = request.POST.get('report', None)
    reportToDel = get_object_or_404(Report, pk=reportId)
    # for attachment in reportToDel.attachment_set.all():
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
            # for attachment in report.attachment_set.all():
            #    attachment.file.save()
            #    attachment.save()
            report.save()
            # form.save()
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
    # create new folder
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
        # raise HTTP404

    folderPk = request.POST.get('folder', None)
    folderToDel = get_object_or_404(Folder, pk=folderPk)
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
    # create new folder
    if request.method == 'POST':
        reportPk = request.POST.get("reportpk", "")
        folderPk = request.POST.get("folderpk", "")
        r = Report.objects.get(pk=reportPk)
        f = Folder.objects.get(pk=folderPk)
        f.report_set.add(r)
        f.save()
        # f.save()
        # r.save()
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
        # f.save()
        # r.save()
    return HttpResponseRedirect(reverse('myapplication.views.manage'))




#NOTE: if user already exists then it jsut resets
def register(request):
    context = RequestContext(request)
    # a boolean value for telling the template whether the registration was successful. Set to False originally, code changes to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)


        # validation checking...
        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)

            user.save()

            # profile = profile_form.save(commit=False)

            #           profile.user = user

            # save the UserProfile model instance/update variable to tell the template registration was successful

            # profile.save()

            registered = True


    else:
        user_form = UserForm()
    # profile_form = UserProfileForm()

    return render_to_response('register.html', {'user_form': user_form, 'registered': registered}, context)


def login_view(request):
    context = RequestContext(request)
    logged_in = False
    invalid_login = False

    if request.method == 'POST':

        # check to see if the post came from the logout in the reports page
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
                    return render_to_response('index.html',
                                              {'login_form': login_form, 'logged_in': logged_in, 'user': user}, context)
            else:
                logger.error('invalid login error message')
                logged_in = False
                invalid_login = True
                login_form = LoginForm()
                return render(request, "login.html",
                              {'login_form': login_form, 'invalid_log': invalid_login, 'logged_in': logged_in})



    else:
        if request.user.is_authenticated():
            logged_in = True
        login_form = LoginForm()

    return render_to_response('login.html', {'login_form': login_form, 'logged_in': logged_in}, context)


from postman.api import pm_write, pm_broadcast
from secureshare.settings import COUNTER



def send_broadcast(request):
    if request.method == 'POST':
        form = BroadcastForm(request.POST)

        # validation checking...
        if form.is_valid():
            sender = request.user

            subject = request.POST['subject']
            text = request.POST['body']
            encrypted = request.POST.get('encrypted', False)
            enc_key = request.POST['enc_key']
            raw_b = b""

            if enc_key == "":
                enc_key = "N/A"
            else:

                #encrypt
                #encrypt
                raw_b = encrypt(enc_key, text)
                text=str(raw_b)

            pm_broadcast(sender,"", subject, encrypted, raw=raw_b, body=text)
            return render(request, 'postman/inbox.html', )
        else:
            return render(request, 'broadcast.html', {'message_form': form})


    else:
        form = BroadcastForm()
        return render(request, 'broadcast.html', {'message_form': form})

from simplecrypt import encrypt, decrypt

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        # validation checking...
        if form.is_valid():
            sender = request.user
            recipient_name = request.POST['recipient']
            try:
                recipient = User.objects.get(username=recipient_name)
            except  User.DoesNotExist:
                error = "User does not exist.  Please enter a valid username"
                return render(request, 'new_message.html', {'message_form': form, "error": error})

            subject = request.POST['subject']
            text = request.POST['body']
            encrypted = request.POST.get('encrypted', False)
            enc_key = request.POST['enc_key']
            raw_b = b""
            if enc_key == "":
                enc_key = "N/A"
            else:
                #encrypt
                raw_b = encrypt(enc_key, text)
                text=str(raw_b)


            pm_write(sender,recipient,subject, encrypted, raw=raw_b, body=text)
            return render(request, 'postman/inbox.html', )
        else:
            # print("invalid form")
            return render(request, 'new_message.html', {'message_form': form })


    else:
        form = MessageForm()
        return render(request, 'new_message.html', {'message_form': form})


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
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
                found_entries = Report.objects.filter(
                    Q(username=request.user.username) | Q(visibility="public")).filter(entry_query).order_by(
                    'timestamp')

        else:
            found_entries = None

        begin = request.GET['begin']
        end = request.GET['end']

        beginMatch = re.match('\d{4}-\d{2}-\d{2}', begin)
        endMatch = re.match('\d{4}-\d{2}-\d{2}', end)
        if beginMatch and endMatch:
            found_entries = found_entries.filter(timestamp__range=[begin, end])
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
            found_entries = Report.objects.filter(Q(username=request.user.username) | Q(visibility="public")).order_by(
                'timestamp')
        begin = request.GET['begin']
        end = request.GET['end']

        beginMatch = re.match('\d{4}-\d{2}-\d{2}', begin)
        endMatch = re.match('\d{4}-\d{2}-\d{2}', end)
        if beginMatch and endMatch:
            found_entries = found_entries.filter(timestamp__range=[begin, end])
            badDate = False
        else:
            badDate = True

        visibilityGet = request.GET['visibility']
        if (visibilityGet == "all"):
            pass
        else:
            found_entries = found_entries.filter(visibility=visibilityGet)

    return render_to_response('search.html',
                              {'query_string': query_string, 'found_entries': found_entries, 'bad_date': badDate},
                              context_instance=RequestContext(request))
