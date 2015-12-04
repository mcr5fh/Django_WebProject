from django.shortcuts import render
from django.http import HttpResponse

import json
import sys

from myapplication.models import Report

test_json = ['hello', {1:'2'}]

def report_to_dict(report):
    result = {}
    result['timestamp'] = str(report.timestamp)
    result['short'] = str(report.short)
    result['detailed'] = str(report.detailed)
    result['url'] = '/media/' + str(report.file)

    return result

def file_list(request):
    report_objs = Report.objects.all()
    reports = map(report_to_dict, report_objs)

    print(request.method + ': ' + str(request.body))
    sys.stdout.flush() # required to print to heroku console

    return HttpResponse(json.dumps(list(reports)))
