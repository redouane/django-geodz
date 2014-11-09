# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Province'
        db.create_table(u'geodz_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('position', self.gf('geoposition.fields.GeopositionField')(default='0,0', max_length=42, null=True, blank=True)),
        ))
        db.send_create_signal(u'geodz', ['Province'])

        # Adding model 'Municipality'
        db.create_table(u'geodz_municipality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('geoposition.fields.GeopositionField')(default='0,0', max_length=42, null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(related_name='municipalities', to=orm['geodz.Province'])),
        ))
        db.send_create_signal(u'geodz', ['Municipality'])


    def backwards(self, orm):
        # Deleting model 'Province'
        db.delete_table(u'geodz_province')

        # Deleting model 'Municipality'
        db.delete_table(u'geodz_municipality')


    models = {
        u'geodz.municipality': {
            'Meta': {'ordering': "['province']", 'object_name': 'Municipality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('geoposition.fields.GeopositionField', [], {'default': "'0,0'", 'max_length': '42', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'municipalities'", 'to': u"orm['geodz.Province']"})
        },
        u'geodz.province': {
            'Meta': {'ordering': "['id']", 'object_name': 'Province'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('geoposition.fields.GeopositionField', [], {'default': "'0,0'", 'max_length': '42', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['geodz']