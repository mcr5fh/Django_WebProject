# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login

from myapp.forms import UserForm
from myapp.models import Report
from myapp.forms import ReportForm
from django.utils import timezone
from myapp.forms import LoginForm

from django.contrib.auth import authenticate, login, logout

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def report_new(request):
    # Handle file upload
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            newReport = form.save(commit=False)
            newReport.timestamp = timezone.now()
            newReport.file = request.FILES['file']
            newReport.save()

            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = ReportForm() # A empty, unbound form
    return render(request, 'report.html', {'form': form})




def list(request):

    # Load documents for the list page
    reports = Report.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'reports': reports,},
        context_instance=RequestContext(request)
    )

def delete(request):
    if request.method != 'POST':
        raise HTTP404

    reportId = request.POST.get('report', None)
    reportToDel = get_object_or_404(Report, pk = reportId)
    if reportToDel.file:
        reportToDel.file.delete()
    reportToDel.delete()

    return HttpResponseRedirect(reverse('myapp.views.list'))

def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.timestamp = timezone.now()
            report.save()

            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = ReportForm(instance=report) # A empty, unbound form
    return render(request, 'report_edit.html', {'form': form, 'report': report})


def makedir(request):
    dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
    os.mkdir(os.path.join('/documents', dirname))
    return HttpResponseRedirect(reverse('myapp.views.list'))


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

def auth_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        #check to see if the post came from the logout in the reports page
        if 'logout' in request.POST:
            logout(request)
            logger.error('Logging out')
            return render(request, 'login.html')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            logger.error('User Found')
            # Redirect to the list of their reports.
            return render(request, 'list.html', {'user_info_dict': request.POST})


        else:
            logger.error('User Not Found')
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'login_failed': True})
    else:
        #show the normal user form when theres not a post
        user_form = UserForm()


    return render_to_response('login.html', {'user_form': user_form,'login_failed': False}, context)


def login_view(request):
    context = RequestContext(request)
    logged_in = False
    
    

    if request.method == 'POST':

        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:

                if user.is_active:
                    login(request, user)
                    logged_in = True
                        # Return to reports page
                    return render_to_response('report.html', {'login_form': login_form,'logged_in': logged_in}, context)
                #else:
                #return 'invalid login error message'
    
                    
    else:
        login_form = LoginForm()
    
    return render_to_response('login.html', {'login_form': login_form,'logged_in': logged_in}, context)









