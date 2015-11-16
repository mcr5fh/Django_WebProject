# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

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

'''
def makedir(request):
    dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45
    os.mkdir(os.path.join('/documents', dirname))

    return HttpResponseRedirect(reverse('myproject.myapp.views.list')) '''