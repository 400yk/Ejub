import MySQLdb
import collections
import json
from django.utils import timezone
import datetime
from ej.models import CoursesList, SkillsList, JobsList
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
        the_field_set = request.GET.getlist("the_field_set[]")
        sub_field_set = request.GET.getlist("sub_field_set[]")
        other_fields_set = request.GET.getlist("other_fields_set[]")
        if field and course_id:
            related_jobs_id = []
            for skill in CoursesList.objects.get(pk = course_id).skillsLists.all():
                # Get all the ids for the related job, now create a sql table to facilitate query group by
                if the_field_set and sub_field_set and len(the_field_set) == len(sub_field_set):
                    kwargs = {}
                    exclude_kwargs = {}
                    for i in range(len(the_field_set)):
                        if sub_field_set[i] != "Other":
                            kwargs['{0}__{1}'.format(the_field_set[i], 'exact')] = sub_field_set[i]
                        else:
                            other_fields_tmp = [str(k.strip().replace('"','')) for k in other_fields_set[i].strip('[]').split(',')]
                            exclude_kwargs['{0}__{1}'.format(the_field_set[i], 'in')] = other_fields_tmp
                    related_jobs_id += [i.id for i in skill.jobslist_set.filter(**kwargs).exclude(**exclude_kwargs)]
                else:
                    related_jobs_id += [ i.id for i in skill.jobslist_set.all()]

            if field == "all":
                pass
            # Need special treatment for date type, rank by recent to old
            elif field == "posted":
                jobs_tmp = JobsList.objects.filter(id__in = related_jobs_id)
                # Use tuple in order to keep the order
                times_count = (('Past week', 0), ('Past month', 0), ('Past quarter', 0), ('Past year', 0), ('Past 3 years', 0), ('3 years older', 0))
                times_count = collections.OrderedDict(times_count)
                for j in jobs_tmp:
                    time_passed = None
                    # Convert to number of days that has passed
                    time_passed =  ((timezone.now() - j.posted).days)
                    if time_passed or time_passed == 0:
                        # Past week
                        if time_passed <= 7:
                            times_count['Past week'] += 1
                        # Past month
                        elif time_passed <= (365 / 12):
                            times_count['Past month'] += 1
                        # Past quarter
                        elif time_passed <= (3 * 365 / 12):
                            times_count['Past quarter'] += 1
                        # Past year
                        elif time_passed <= 365.25:
                            times_count['Past year'] += 1
                        # Past three years
                        elif time_passed <= 3 * 365.25:
                            times_count['Past three years'] += 1
                        # More than three years from now
                        else:
                            times_count['3 years older'] += 1
                    
                top_counts = [{'count':v, 'field': k} for k,v in times_count.iteritems()]

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
                    # Add the name of other fields in case user click on 'Other'
                    other_fields = [f[field] for f in top_counts]
                    top_counts.append({'count': count_other, field: 'Other', 'other_fields': json.dumps(other_fields)})
                # Rename the key to a common name for easier accessment in html
                # print top_counts
                for each in top_counts:
                    each['field'] = each.pop(field)
    print top_counts
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
        other_fields = request.GET.getlist("other_fields_set[]")
        course_id = request.GET["course_id"]
        if course_id and len(sub_field) == len(field):
            # Find the jobs that meet sub_field requirement
            kwargs = {}
            exclude_kwargs = {}
            for i in range(len(sub_field)):
                # Need special treatment for posted filter
                if field[i] == 'posted':
                    if sub_field[i] == 'Past week':
                        kwargs['{0}__{1}'.format(field[i], 'gte')] = timezone.now() - datetime.timedelta(days = 7)
                    elif sub_field[i] == 'Past month':
                        kwargs['{0}__{1}'.format(field[i], 'lt')] = timezone.now() - datetime.timedelta(days = 7)
                        kwargs['{0}__{1}'.format(field[i], 'gte')] = timezone.now() - datetime.timedelta(days = 31)
                    elif sub_field[i] == 'Past quarter':
                        kwargs['{0}__{1}'.format(field[i], 'lt')] = timezone.now() - datetime.timedelta(days = 31)
                        kwargs['{0}__{1}'.format(field[i], 'gte')] = timezone.now() - datetime.timedelta(days = 92)
                    elif sub_field[i] == 'Past year':
                        kwargs['{0}__{1}'.format(field[i], 'lt')] = timezone.now() - datetime.timedelta(days = 92)
                        kwargs['{0}__{1}'.format(field[i], 'gte')] = timezone.now() - datetime.timedelta(days = 365)
                    elif sub_field[i] == 'Past 3 years':
                        kwargs['{0}__{1}'.format(field[i],'lt')] = timezone.now() - datetime.timedelta(days = 365)
                        kwargs['{0}__{1}'.format(field[i],'gte')] = timezone.now() - datetime.timedelta(days = 365 * 3)
                    elif sub_field[i] == '3 years older':
                        kwargs['{0}__{1}'.format(field[i], 'lt')] = timezone.now() - datetime.timedelta(days = 365 * 3)
                else:
                    # If sub_field isn't other, do the regular filtering
                    if sub_field[i] != 'Other':
                        kwargs['{0}__{1}'.format(field[i], 'exact')] = sub_field[i]
                    else:
                       # each element in other_fields is in unicode, need to convert it to string
                        other_fields_tmp = [str(k.strip().replace('"', '')) for k in other_fields[i].strip('[]').split(",")]
     
                        exclude_kwargs['{0}__{1}'.format(field[i], 'in')] = other_fields_tmp

            related_jobs = sort_by_relevance(CoursesList.objects.get(pk = course_id).skillsLists.all(), max_jobs, kwargs, exclude_kwargs)

    return render_to_response('ej/update_related_jobs.html', {'related_jobs': related_jobs}, context)

def sort_by_relevance(skill_set, max_jobs = 15, kwargs = {}, exclude_kwargs = {}):
    related_jobs_id = []
    related_jobs = []
    if not exclude_kwargs:
        if kwargs:
            for skill in skill_set:
                related_jobs_id += [i.id for i in skill.jobslist_set.filter(**kwargs)]
        else:
            for skill in skill_set: 
               related_jobs_id += [i.id for i in skill.jobslist_set.all()]
    # If the user selected "Other"
    else:
        print exclude_kwargs
        if kwargs:
            for skill in skill_set:
                related_jobs_id += [i.id for i in skill.jobslist_set.filter(**kwargs).exclude(**exclude_kwargs)]
        else:
            for skill in skill_set:
                related_jobs_id += [i.id for i in skill.jobslist_set.exclude(**exclude_kwargs)]
        
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
    
    json_skills = json.dumps({"skills_id": skills_id})
    return HttpResponse(json_skills, content_type="application/json")

def skills(request):
    context = RequestContext(request)
    top_skills_industry = SkillsList.objects.all().annotate(count = Count('jobslist')).order_by('-count')[:15]
    top_skills_college = SkillsList.objects.all().annotate(count = Count('courseslist')).order_by('-count')[:15]
    return render_to_response('ej/skills.html', {'top_skills_industry': top_skills_industry, 'top_skills_college': top_skills_college}, context)
