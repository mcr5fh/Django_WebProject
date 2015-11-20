# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^delete/$', 'delete', name='delete'),
    url(r'^register/$', 'register', name='register'),
    url(r'^report/$', 'report_new', name ='report'),
    url(r'^report/(?P<pk>[0-9]+)/edit/$', 'report_edit', name='report_edit'),
    url(r'^login/$', 'auth_login', name ='login'),
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