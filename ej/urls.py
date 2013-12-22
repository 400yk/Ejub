from django.conf.urls import patterns, url
from ej import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        )
