# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from postman.views import WriteView

urlpatterns = patterns('myapplication.views',
    url(r'^index/$', 'index', name='index'),
    url(r'^list/$', 'list', name='list'),
    url(r'^delete/$', 'delete', name='delete'),
    url(r'^register/$', 'register', name='register'),
    url(r'^login/$','login_view', name='login'),
    url(r'^report/$', 'report_new', name ='report'),
   # url(r'^report_folder/$', 'report_folder_new', name ='report_folder'),
    #TODO: Report folder edit
    url(r'^write/$', 'send_message', name='send_m'),

    url(r'^report/(?P<pk>[0-9]+)/edit/$', 'report_edit', name='report_edit'),
    url(r'^manage/$', 'manage', name='manage'),
    url(r'^folder_new/$', 'folder_new', name='folder_new'),
    url(r'^folder_delete/$', 'folder_delete', name='folder_delete'),
    url(r'^move_report/$', 'move_report', name='move_report'),
    #url(r'^login/$', 'auth_login', name ='login'),
)


''' Create a folder
        <form action="(% url "makedir" %)" method ="post" enctype="multipart/form-data">
        (% csrf_token %)
        <p><input type="submit" value="Make Directory" /></p>
        -->
        <!-- Manage reports -->

    <!-- <form action="{% url "delete" %}" method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    <input type="hidden" name="docfile" value="{{ document.pk }}" />
                     <input type="submit" value="Delete" />
                </form> '''