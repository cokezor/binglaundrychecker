# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field machines on 'Building'
        db.delete_table(db.shorten_name(u'laundry_building_machines'))

        # Adding M2M table for field sides on 'Building'
        m2m_table_name = db.shorten_name(u'laundry_building_sides')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False)),
            ('side', models.ForeignKey(orm[u'laundry.side'], null=False))
        ))
        db.create_unique(m2m_table_name, ['building_id', 'side_id'])


    def backwards(self, orm):
        # Adding M2M table for field machines on 'Building'
        m2m_table_name = db.shorten_name(u'laundry_building_machines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False)),
            ('machine', models.ForeignKey(orm[u'laundry.machine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['building_id', 'machine_id'])

        # Removing M2M table for field sides on 'Building'
        db.delete_table(db.shorten_name(u'laundry_building_sides'))


    models = {
        u'laundry.building': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sides': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.Side']", 'symmetrical': 'False'})
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