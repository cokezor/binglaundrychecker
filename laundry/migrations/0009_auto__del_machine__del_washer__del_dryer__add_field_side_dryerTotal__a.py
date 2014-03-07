# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Machine'
        db.delete_table(u'laundry_machine')

        # Deleting model 'Washer'
        db.delete_table(u'laundry_washer')

        # Deleting model 'Dryer'
        db.delete_table(u'laundry_dryer')

        # Adding field 'Side.dryerTotal'
        db.add_column(u'laundry_side', 'dryerTotal',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Side.dryerAvail'
        db.add_column(u'laundry_side', 'dryerAvail',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Side.dryerTimes'
        db.add_column(u'laundry_side', 'dryerTimes',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default='1,', max_length=20),
                      keep_default=False)

        # Adding field 'Side.washerTotal'
        db.add_column(u'laundry_side', 'washerTotal',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Side.washerAvail'
        db.add_column(u'laundry_side', 'washerAvail',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Side.washerTimes'
        db.add_column(u'laundry_side', 'washerTimes',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default='1,', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Machine'
        db.create_table(u'laundry_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numTotal', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('numAvail', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'laundry', ['Machine'])

        # Adding model 'Washer'
        db.create_table(u'laundry_washer', (
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laundry.Side'], null=True)),
            (u'machine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['laundry.Machine'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'laundry', ['Washer'])

        # Adding model 'Dryer'
        db.create_table(u'laundry_dryer', (
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laundry.Side'], null=True)),
            (u'machine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['laundry.Machine'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'laundry', ['Dryer'])

        # Deleting field 'Side.dryerTotal'
        db.delete_column(u'laundry_side', 'dryerTotal')

        # Deleting field 'Side.dryerAvail'
        db.delete_column(u'laundry_side', 'dryerAvail')

        # Deleting field 'Side.dryerTimes'
        db.delete_column(u'laundry_side', 'dryerTimes')

        # Deleting field 'Side.washerTotal'
        db.delete_column(u'laundry_side', 'washerTotal')

        # Deleting field 'Side.washerAvail'
        db.delete_column(u'laundry_side', 'washerAvail')

        # Deleting field 'Side.washerTimes'
        db.delete_column(u'laundry_side', 'washerTimes')


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
            'dryerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20'}),
            'dryerTotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'washerAvail': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'washerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20'}),
            'washerTotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['laundry']