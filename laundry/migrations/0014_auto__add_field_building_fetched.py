# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Building.fetched'
        db.add_column(u'laundry_building', 'fetched',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Building.fetched'
        db.delete_column(u'laundry_building', 'fetched')


    models = {
        u'laundry.building': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Building'},
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Community']", 'null': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'laundry.community': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'laundry.side': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Side'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Building']", 'null': 'True'}),
            'dryerAvail': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dryerComplete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dryerInUse': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dryerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '255', 'null': 'True'}),
            'dryerTotal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'washerAvail': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'washerComplete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'washerInUse': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'washerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '255', 'null': 'True'}),
            'washerTotal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['laundry']