import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ejub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/ej/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ej/', include('ej.urls', namespace = 'ej')),
    url(r'^accounts/', include('allauth.urls')),
)

