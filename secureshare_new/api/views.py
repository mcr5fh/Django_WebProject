from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.db.models import Q

import json
import sys

from base64 import b64decode

from myapplication.models import Report

test_json = ['hello', {1:'2'}]

def report_to_dict(report):
    result = {}
    result['timestamp'] = str(report.timestamp)
    result['short'] = str(report.short)
    result['detailed'] = str(report.detailed)
    result['file1'] = '/media/' + str(report.file1) if report.file1 else ''
    result['file2'] = '/media/' + str(report.file2) if report.file2 else ''
    result['file3'] = '/media/' + str(report.file3) if report.file3 else ''
    result['file4'] = '/media/' + str(report.file4) if report.file4 else ''
    result['file5'] = '/media/' + str(report.file5) if report.file5 else ''

    return result

def file_list(request):
    if 'HTTP_AUTHORIZATION' not in request.META:
        return HttpResponse('login failed')

    encoded_auth = request.META['HTTP_AUTHORIZATION']
    auth = b64decode(encoded_auth.split()[-1]).decode('utf-8')

    [username, password] = auth.split(':')
    user = authenticate(username=username, password=password)

    if user is not None:
        #report_objs = Report.objects.all()
        report_objs = Report.objects.filter(Q(username=username) | Q(visibility="public"))
        reports = map(report_to_dict, report_objs)
        return HttpResponse(json.dumps(list(reports)))
        #return HttpResponse('It worked!')
    else:
        return HttpResponse('login failed')
