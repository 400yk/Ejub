from django.conf.urls import patterns, url
from ej import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        url(r'^skills/', views.skills, name = 'skills'),
        url(r'^courses/', views.courses, name = 'courses'),
        url(r'^jobs/', views.jobs, name = 'jobs'),
        url(r'^job_search/', views.job_search, name = 'job_search'),
        url(r'^job_detail/(?P<job_id>\d+)/$', views.job_detail, name = 'job_detail'),
        url(r'^course_search/', views.course_search, name = 'course_search'),
        url(r'^course_detail/(?P<course_id>\d+)/$', views.course_detail, name = 'course_detail'),
        url(r'^from_skill_find_courses/', views.from_skill_find_courses),
        url(r'^quick_ref_course_detail/', views.quick_ref_course_detail),
        url(r'^get_jobs/', views.get_jobs),
        url(r'^filter_jobs/', views.filter_jobs),
        url(r'^from_job_get_skill', views.from_job_get_skill),
        )




