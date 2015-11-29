# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from myapplication.forms import UserForm
from myapplication.models import Report
from myapplication.forms import ReportForm
from django.utils import timezone
from myapplication.forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@login_required
def index(request):
      return render(request, 'index.html')

@login_required
def report_new(request):
    logger.error("User in request: " + request.user.username)
    # Handle file upload
    if request.method == 'POST':
        #logger.error("User in request: " + request.user.username)
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            newReport = form.save(commit=False)
            newReport.timestamp = timezone.now()
            #if request.FILES['file']:
            #   newReport.file = request.FILES['file']
            newReport.save()

            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapplication.views.list'))
    else:
        form = ReportForm() # A empty, unbound form
    return render(request, 'report.html', {'form': form})



@login_required
def list(request):

    # Load documents for the list page
    reports = Report.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'reports': reports,},
        context_instance=RequestContext(request)
    )

@login_required
def delete(request):
    if request.method != 'POST':
        logger.log("METHOD NOT POST")
        #raise HTTP404

    reportId = request.POST.get('report', None)
    reportToDel = get_object_or_404(Report, pk = reportId)
    if reportToDel.file:
        reportToDel.file.delete()
    reportToDel.delete()

    return HttpResponseRedirect(reverse('myapplication.views.list'))

@login_required
def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.timestamp = timezone.now()
            report.save()

            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myapplication.views.list'))
    else:
        form = ReportForm(instance=report) # A empty, unbound form
    return render(request, 'report_edit.html', {'form': form, 'report': report})

@login_required
def makedir(request):
    dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
    os.mkdir(os.path.join('/documents', dirname))
    return HttpResponseRedirect(reverse('myapplication.views.list'))


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

'''
def logout_view(request):
    if request.method == 'POST':

         #check to see if the post came from the logout in the reports page
        if 'logout' in request.POST:
            logout(request)
            logger.error('Logging out')
            login_form = LoginForm('','')
            return render(request, 'login.html', {'login_form': login_form})
'''

def login_view(request):
    context = RequestContext(request)
    logged_in = False

    if request.method == 'POST':

         #check to see if the post came from the logout in the reports page
        if 'logout' in request.POST:
            logout(request)
            logger.error('Logging out')
            login_form = LoginForm('','')
            return render(request, 'login.html', {'login_form': login_form})

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
    
                    
    else:
        if request.user.is_authenticated():
            logged_in = True
        login_form = LoginForm()
    
    return render_to_response('login.html', {'login_form': login_form,'logged_in': logged_in}, context)








