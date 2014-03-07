# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Side'
        db.create_table(u'laundry_side', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('locationId', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'laundry', ['Side'])


    def backwards(self, orm):
        # Deleting model 'Side'
        db.delete_table(u'laundry_side')


    models = {
        u'laundry.building': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'machines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.Machine']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.community': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Community'},
            'buildings': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.Building']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.machine': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Machine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.side': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Side'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['laundry']