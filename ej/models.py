# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class SkillsList(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) 
    skill = models.CharField(max_length=255)

    def __unicode__(self):
        return self.skill

    class Meta:
        managed = True
        db_table = 'skills_list'

class CoursesList(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    coursedescription = models.TextField(db_column='courseDescription', blank=True) 
    courseuid = models.CharField(db_column='courseUID', max_length=30, blank=True) 
    coursetitle = models.CharField(db_column='courseTitle', max_length=255, blank=True) 
    upperunits = models.IntegerField(db_column='upperUnits', blank=True, null=True) 
    uri = models.URLField(blank=True)
    lowerunits = models.IntegerField(db_column='lowerUnits', blank=True, null=True) 
    departmentcode = models.CharField(db_column='departmentCode', max_length=30, blank=True) 
    coursenumber = models.CharField(db_column='courseNumber', max_length=30, blank=True) 
    subdepartmentcode = models.CharField(db_column='subDepartmentCode', max_length=30, blank=True) 

    skillsLists = models.ManyToManyField(SkillsList)

    def __unicode__(self):
        return self.coursetitle

    class Meta:
        managed = True
        db_table = 'courses_list'

class JobsList(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) 
    job_id = models.IntegerField()
    city = models.CharField(db_column='City', max_length=50, blank=True) 
    region = models.CharField(db_column='Region', max_length=50, blank=True) 
    country = models.CharField(db_column='Country', max_length=50, blank=True) 
    company = models.CharField(db_column='Company', max_length=100, blank=True) 
    description = models.TextField(db_column='Description', blank=True) 
    title = models.CharField(db_column='Title', max_length=100, blank=True) 
    experience = models.CharField(db_column='Experience', max_length=100, blank=True) 
    skills = models.TextField(db_column='Skills', blank=True) 
    posted = models.DateTimeField(db_column='Posted', blank=True, null=True) 
    employmenttype = models.CharField(db_column='EmploymentType', max_length=50, blank=True) 
    functions = models.CharField(db_column='Functions', max_length=100, blank=True) 
    industry = models.CharField(db_column='Industry', max_length=150, blank=True) 

    skillsLists = models.ManyToManyField(SkillsList)

    def __unicode__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'jobs_list'

