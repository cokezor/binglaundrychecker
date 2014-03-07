# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field laundryRooms on 'Community'
        db.delete_table(db.shorten_name(u'laundry_community_laundryRooms'))

        # Adding M2M table for field buildings on 'Community'
        m2m_table_name = db.shorten_name(u'laundry_community_buildings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('community', models.ForeignKey(orm[u'laundry.community'], null=False)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False))
        ))
        db.create_unique(m2m_table_name, ['community_id', 'building_id'])


    def backwards(self, orm):
        # Adding M2M table for field laundryRooms on 'Community'
        m2m_table_name = db.shorten_name(u'laundry_community_laundryRooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('community', models.ForeignKey(orm[u'laundry.community'], null=False)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False))
        ))
        db.create_unique(m2m_table_name, ['community_id', 'building_id'])

        # Removing M2M table for field buildings on 'Community'
        db.delete_table(db.shorten_name(u'laundry_community_buildings'))


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
        }
    }

    complete_apps = ['laundry']