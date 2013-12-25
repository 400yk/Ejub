from django.conf.urls import patterns, url
from ej import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        url(r'^skills/', views.skills, name = 'skills'),
        url(r'^courses/', views.courses, name = 'courses'),
        url(r'^jobs/', views.jobs, name = 'jobs'),
        url(r'^course_search/', views.course_search, name = 'course_search'),
        url(r'^course_detail/(?P<course_id>\d+)/$', views.course_detail, name = 'course_detail'),
        )

