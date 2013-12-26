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
    context = RequestContext(request)
    return render_to_response('ej/jobs.html', context)


def get_job(max_jobs = 0, starts_with = {}):
    job_list = []
    if starts_with:
        filterargs = {}
        # Create the filter that has all the input fields as searches
        for k,v in starts_with.iteritems():
            if v:
                # Ignore case
                filterargs['{0}__{1}'.format(k, 'icontains')] = v
        
        if filterargs:
            job_list = JobsList.objects.filter(**filterargs)
        else:
            job_list = JobsList.objects.all()
    else:
        job_list = JobsList.objects.all()

    if max_jobs > 0:
        if len(job_list) > max_jobs:
            job_list = job_list[:max_jobs]

    return job_list

def job_search(request):
    context = RequestContext(request)
    starts_with = ''
    job_list = []
    
    field_list = ['title', 'company', 'country', 'city']
    starts_with = {}

    if request.method == "GET":
        for field in field_list:
            starts_with[field] = request.GET['search_' + field]
    else:
        for field in field_list:
            starts_with[field] = request.POST['search_' + field]

    job_list = get_job(15, starts_with)
    return render_to_response('ej/job_search.html', {'job_list': job_list}, context)


def get_course(max_courses = 0, starts_with = {}):
    course_list = []
    if starts_with:
        filterargs = {}
        # Create the filter that has all the input fields as searches
        for k,v in starts_with.iteritems():
            if v:
                # Ignore case
                filterargs['{0}__{1}'.format(k, 'icontains')] = v
        
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
    
    field_list = ['coursetitle', 'departmentcode', 'courseuid']
    starts_with = {}

    if request.method == "GET":
        for field in field_list:
            starts_with[field] = request.GET['search_' + field]
    else:
        for field in field_list:
            starts_with[field] = request.POST['search_' + field]

    course_list = get_course(15, starts_with)
    return render_to_response('ej/course_search.html', {'course_list': course_list}, context)

# Once the user finds the course, retrieve the course detail
def course_detail(request, course_id):
    context = RequestContext(request)
    course = {}
    related_jobs = []
    # The maximum amount of related jobs that can be shown
    max_jobs = 15
    if course_id:
        course = CoursesList.objects.get(pk = course_id)
        for skill in course.skillsLists.all():
            if len(related_jobs) <= max_jobs:
                related_jobs += skill.jobslist_set.all()
            else:
                break
        print related_jobs
        if len(related_jobs) > max_jobs:
            related_jobs = related_jobs[:max_jobs]
    return render_to_response('ej/course_detail.html', {'course': course, 'related_jobs': related_jobs}, context) 


# Once the user finds the course, retrieve the course detail
def job_detail(request, job_id):
    context = RequestContext(request)
    job = {}
    related_courses = []
    # The maximum amount of related jobs that can be shown
    max_courses = 15
    if job_id:
        job = JobsList.objects.get(pk = job_id)
        for skill in job.skillsLists.all():
            if len(related_courses) <= max_courses:
                related_courses += skill.courseslist_set.all()
            else:
                break
        if len(related_courses) > max_courses:
            related_courses = related_courses[:max_courses]
    return render_to_response('ej/job_detail.html', {'job': job, 'related_courses': related_courses}, context) 

def from_skill_find_courses(request):
    context = RequestContext(request)
    courses = []
    max_courses = 15
    skill = {}
    if request.method == "GET":
        skill_id = request.GET['skill_id']
        if skill_id:
            skill = SkillsList.objects.get(pk = skill_id)
            courses += skill.courseslist_set.all()
            print courses
            if len(courses) > max_courses:
                courses = courses[:max_courses]
    else:
        skill_id = request.POST['skill_id']

    return render_to_response('ej/from_skill_find_courses.html', {'courses': courses, 'skill': skill}, context)
