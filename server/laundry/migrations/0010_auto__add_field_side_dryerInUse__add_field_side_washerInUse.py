# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Side.dryerInUse'
        db.add_column(u'laundry_side', 'dryerInUse',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Side.washerInUse'
        db.add_column(u'laundry_side', 'washerInUse',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Side.dryerInUse'
        db.delete_column(u'laundry_side', 'dryerInUse')

        # Deleting field 'Side.washerInUse'
        db.delete_column(u'laundry_side', 'washerInUse')


    models = {
        u'laundry.building': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Building'},
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Community']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.community': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.side': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Side'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Building']", 'null': 'True'}),
            'dryerAvail': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'dryerInUse': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'dryerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20'}),
            'dryerTotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'washerAvail': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'washerInUse': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'washerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20'}),
            'washerTotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['laundry']