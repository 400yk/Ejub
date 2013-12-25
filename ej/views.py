from ej.models import CoursesList, SkillsList, JobsList
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse

def home(request):
    context = RequestContext(request)
    return render_to_response('ej/home.html', context)

def courses(request):
    context = RequestContext(request)
    return render_to_response('ej/courses.html', context)

def skills(request):
    pass

def jobs(request):
    pass

def get_course(max_courses = 0, starts_with = {}):
    course_list = []
    if starts_with:
        filterargs = {}
        # Create the filter that has all the input fields as searches
        for k,v in starts_with.iteritems():
            if v:
                # Ignore case
                filterargs['{0}__{1}'.format(k, 'istartswith')] = v
        
        if filterargs:
            course_list = CoursesList.objects.filter(**filterargs)
        else:
            course_list = CoursesList.objects.all()
    else:
        course_list = CoursesList.objects.all()

    if max_courses > 0:
        if len(course_list) > max_courses:
            course_list = course_list[:max_courses]

    return course_list

def course_search(request):
    context = RequestContext(request)
    starts_with = ''
    course_list = []
    
    field_list = ['coursetitle', 'departmentcode']
    starts_with = {}

    if request.method == "GET":
        for field in field_list:
            starts_with[field] = request.GET['search_' + field]
    else:
        for field in field_list:
            starts_with[field] = request.POST['search_' + field]

    course_list = get_course(8, starts_with)
    return render_to_response('ej/course_search.html', {'course_list': course_list}, context)

# Once the user finds the course, retrieve the course detail
def course_detail(request, course_id):
    context = RequestContext(request)
    course = {}
    if course_id:
        course = CoursesList.objects.get(pk = course_id)
        
    return render_to_response('ej/course_detail.html', {'course': course}, context) 
