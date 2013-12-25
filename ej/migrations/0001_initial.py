# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SkillsList'
        db.create_table(u'skills_list', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ej', ['SkillsList'])

        # Adding model 'CoursesList'
        db.create_table(u'courses_list', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('coursedescription', self.gf('django.db.models.fields.TextField')(db_column=u'courseDescription', blank=True)),
            ('courseuid', self.gf('django.db.models.fields.CharField')(max_length=30, db_column=u'courseUID', blank=True)),
            ('coursetitle', self.gf('django.db.models.fields.CharField')(max_length=255, db_column=u'courseTitle', blank=True)),
            ('upperunits', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'upperUnits', blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('lowerunits', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'lowerUnits', blank=True)),
            ('departmentcode', self.gf('django.db.models.fields.CharField')(max_length=30, db_column=u'departmentCode', blank=True)),
            ('coursenumber', self.gf('django.db.models.fields.CharField')(max_length=30, db_column=u'courseNumber', blank=True)),
            ('subdepartmentcode', self.gf('django.db.models.fields.CharField')(max_length=30, db_column=u'subDepartmentCode', blank=True)),
        ))
        db.send_create_signal(u'ej', ['CoursesList'])

        # Adding M2M table for field skillsLists on 'CoursesList'
        m2m_table_name = db.shorten_name(u'courses_list_skillsLists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('courseslist', models.ForeignKey(orm[u'ej.courseslist'], null=False)),
            ('skillslist', models.ForeignKey(orm[u'ej.skillslist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['courseslist_id', 'skillslist_id'])

        # Adding model 'JobsList'
        db.create_table(u'jobs_list', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('job_id', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'City', blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'Region', blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'Country', blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Company', blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(db_column=u'Description', blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Title', blank=True)),
            ('experience', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Experience', blank=True)),
            ('skills', self.gf('django.db.models.fields.TextField')(db_column=u'Skills', blank=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'Posted', blank=True)),
            ('employmenttype', self.gf('django.db.models.fields.CharField')(max_length=50, db_column=u'EmploymentType', blank=True)),
            ('functions', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'Functions', blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=60, db_column=u'Industry', blank=True)),
        ))
        db.send_create_signal(u'ej', ['JobsList'])

        # Adding M2M table for field skillsLists on 'JobsList'
        m2m_table_name = db.shorten_name(u'jobs_list_skillsLists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('jobslist', models.ForeignKey(orm[u'ej.jobslist'], null=False)),
            ('skillslist', models.ForeignKey(orm[u'ej.skillslist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['jobslist_id', 'skillslist_id'])


    def backwards(self, orm):
        # Deleting model 'SkillsList'
        db.delete_table(u'skills_list')

        # Deleting model 'CoursesList'
        db.delete_table(u'courses_list')

        # Removing M2M table for field skillsLists on 'CoursesList'
        db.delete_table(db.shorten_name(u'courses_list_skillsLists'))

        # Deleting model 'JobsList'
        db.delete_table(u'jobs_list')

        # Removing M2M table for field skillsLists on 'JobsList'
        db.delete_table(db.shorten_name(u'jobs_list_skillsLists'))


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
            'functions': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "u'Functions'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "u'Industry'", 'blank': 'True'}),
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