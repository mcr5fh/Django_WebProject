"""secureshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from myapplication import views

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapplication/',include('myapplication.urls')),
    url(r'^$', RedirectView.as_view(url='/myapplication/index/', permanent=True)),
    #This makes is so that the login redirect goes to the proper login page
    url(r'^accounts/', RedirectView.as_view(url='/myapplication/login/', permanent=True)),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
