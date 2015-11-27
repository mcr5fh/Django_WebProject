from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from myapp import views

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/',include('myapp.urls')),   #, namespace='myapp')),
    url(r'^$', RedirectView.as_view(url='/myapp/list/', permanent=True)),
    #url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
