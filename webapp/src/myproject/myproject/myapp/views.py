# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404


#from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from myproject.myapp.forms import UserForm
from myproject.myapp.models import Report
from myproject.myapp.forms import ReportForm
from django.utils import timezone


def report_new(request):
    # Handle file upload
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            newReport = form.save(commit=False)
            newReport.timestamp = timezone.now()
            newReport.save()

            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
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

    return HttpResponseRedirect(reverse('myproject.myapp.views.list'))

def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            report.timestamp = timezone.now()
            report.save()

            # Redirect to the report list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = ReportForm(instance=report) # A empty, unbound form
    return render(request, 'report_edit.html', {'form': form, 'report': report})


def makedir(request):
    dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
    os.mkdir(os.path.join('/documents', dirname))
    return HttpResponseRedirect(reverse('myproject.myapp.views.list'))


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
















#=======
#return HttpResponseRedirect(reverse('myproject.myapp.views.list')) '''
#>>>>>>> 5c30f052c849f3963fe3dd43f112a2ba3bba2d7f
