import MySQLdb
import collections
from ej.models import CoursesList, SkillsList, JobsList
from django.utils import simplejson
from django.db.models import Sum, Count
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


def search_job(max_jobs = 0, starts_with = {}):
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

    job_list = search_job(15, starts_with)
    return render_to_response('ej/job_search.html', {'job_list': job_list}, context)


def search_course(max_courses = 0, starts_with = {}):
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

    course_list = search_course(15, starts_with)
    return render_to_response('ej/course_search.html', {'course_list': course_list}, context)

# Once the user finds the course, retrieve the course detail
def course_detail(request, course_id):
    context = RequestContext(request)
    course = {}
    related_jobs = []
    related_jobs_id = []
    # The maximum amount of related jobs that can be shown
    max_jobs = 15
    if course_id:
        course = CoursesList.objects.get(pk = course_id)
        related_jobs = sort_by_relevance(course.skillsLists.all(), max_jobs)

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

def quick_ref_course_detail(request):
    context = RequestContext(request)
    course_id = 0
    if request.method == "GET":
        course_id = request.GET['course_id'] 

    return render_to_response('ej/quick_ref_course_detail.html', {'course_id': course_id}, context)

def get_jobs(request):
    context = RequestContext(request)
    # The maximum amount of categories that can be shown in the quick navigation bar
    max_counts = 6
    top_counts = []
    course_id = 0
    field = None
    if request.method == "GET":
        field = request.GET['field']
        course_id = request.GET['course_id']
        if field and course_id:
            related_jobs_id = []
            for skill in CoursesList.objects.get(pk = course_id).skillsLists.all():
                # Get all the ids for the related job, now create a sql table to facilitate query group by
                related_jobs_id += [ i.id for i in skill.jobslist_set.all()]

            if field == "all":
                pass
            else:
                top_counts = JobsList.objects.filter(id__in = related_jobs_id)\
                        .values(field) \
                        .annotate(count = Count('id')) \
                        .order_by('-count')
                
                # If more than max_counts category, group the extra into "others"
                if len(top_counts) > max_counts:
                    other_counts = top_counts[(max_counts-1):]
                    count_other = 0
                    for each in other_counts:
                        count_other += each['count']
                    top_counts = top_counts[:(max_counts-1)]
                    top_counts.append({'count': count_other, field: 'Other'})
                    # Rename the key to a common name for easier accessment in html
                    # print top_counts
                    for each in top_counts:
                        each['field'] = each.pop(field)


    return render_to_response('ej/quick_ref_field_counts.html', {'top_counts': top_counts, 'course_id': course_id, 'the_field': field}, context)
        
# Update the "Related jobs" column when user clicks on sub-field in the quick-reference
def filter_jobs(request):
    context = RequestContext(request)
    sub_field = None
    field = None
    course_id = 0
    max_jobs = 15
    related_jobs = []
    if request.method == "GET":
        sub_field = request.GET.getlist("sub_field_set[]")
        field = request.GET.getlist("the_field_set[]")
        course_id = request.GET["course_id"]
        if course_id and len(sub_field) == len(field):
            # Find the jobs that meet sub_field requirement
            kwargs = {}
            for i in range(len(sub_field)):
                kwargs['{0}__{1}'.format(field[i], 'exact')] = sub_field[i]
            related_jobs = sort_by_relevance(CoursesList.objects.get(pk = course_id).skillsLists.all(), max_jobs, kwargs)


    return render_to_response('ej/update_related_jobs.html', {'related_jobs': related_jobs}, context)

def sort_by_relevance(skill_set, max_jobs = 15, kwargs = {}):
    related_jobs_id = []
    related_jobs = []
    if kwargs:
        for skill in skill_set:
            related_jobs_id += [i.id for i in skill.jobslist_set.filter(**kwargs)]
    else:
        for skill in skill_set: 
           related_jobs_id += [i.id for i in skill.jobslist_set.all()]
    
    # Sort the jobs by the maximum number of matches in skills
    counter = collections.Counter(related_jobs_id)
    related_jobs_id = [job_id for job_id, count in counter.most_common(max_jobs)]
    for best_match in related_jobs_id:
        related_jobs.append(JobsList.objects.get(pk = best_match))

    return related_jobs

   

def from_job_get_skill(request):
    skills_id = []
    if request.method == "GET":
        job_id = request.GET['job_id']
        if job_id:
            job = JobsList.objects.filter(job_id = job_id)
            if job:
                job = job[0]
                skills = job.skillsLists.all()
                skills_id = [s.id for s in skills]
    
    json_skills = simplejson.dumps({"skills_id": skills_id})
    return HttpResponse(json_skills, content_type="application/json")

