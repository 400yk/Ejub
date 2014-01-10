# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'JobsList.functions'
        db.alter_column(u'jobs_list', u'Functions', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Functions'))

        # Changing field 'JobsList.industry'
        db.alter_column(u'jobs_list', u'Industry', self.gf('django.db.models.fields.CharField')(max_length=150, db_column=u'Industry'))

    def backwards(self, orm):

        # Changing field 'JobsList.functions'
        db.alter_column(u'jobs_list', u'Functions', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'Functions'))

        # Changing field 'JobsList.industry'
        db.alter_column(u'jobs_list', u'Industry', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'Industry'))

    models = {
        u'ej.courseslist': {
            'Meta': {'object_name': 'CoursesList', 'db_table': "u'courses_list'"},
            'coursedescription': ('django.db.models.fields.TextField', [], {'db_column': "u'courseDescription'", 'blank': 'True'}),
            'coursenumber': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'courseNumber'", 'blank': 'True'}),
            'coursetitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'courseTitle'", 'blank': 'True'}),
            'courseuid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'courseUID'", 'blank': 'True'}),
            'departmentcode': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'departmentCode'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lowerunits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'lowerUnits'", 'blank': 'True'}),
            'skillsLists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ej.SkillsList']", 'symmetrical': 'False'}),
            'subdepartmentcode': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'subDepartmentCode'", 'blank': 'True'}),
            'upperunits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'upperUnits'", 'blank': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'ej.jobslist': {
            'Meta': {'object_name': 'JobsList', 'db_table': "u'jobs_list'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'City'", 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Company'", 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'Country'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "u'Description'", 'blank': 'True'}),
            'employmenttype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'EmploymentType'", 'blank': 'True'}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Experience'", 'blank': 'True'}),
            'functions': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Functions'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "u'Industry'", 'blank': 'True'}),
            'job_id': ('django.db.models.fields.IntegerField', [], {}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'Posted'", 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'Region'", 'blank': 'True'}),
            'skills': ('django.db.models.fields.TextField', [], {'db_column': "u'Skills'", 'blank': 'True'}),
            'skillsLists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ej.SkillsList']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Title'", 'blank': 'True'})
        },
        u'ej.skillslist': {
            'Meta': {'object_name': 'SkillsList', 'db_table': "u'skills_list'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ej']