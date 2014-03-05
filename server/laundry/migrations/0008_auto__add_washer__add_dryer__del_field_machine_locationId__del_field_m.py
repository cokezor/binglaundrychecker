# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Washer'
        db.create_table(u'laundry_washer', (
            (u'machine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['laundry.Machine'], unique=True, primary_key=True)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laundry.Side'], null=True)),
        ))
        db.send_create_signal(u'laundry', ['Washer'])

        # Adding model 'Dryer'
        db.create_table(u'laundry_dryer', (
            (u'machine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['laundry.Machine'], unique=True, primary_key=True)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laundry.Side'], null=True)),
        ))
        db.send_create_signal(u'laundry', ['Dryer'])

        # Removing M2M table for field buildings on 'Community'
        db.delete_table(db.shorten_name(u'laundry_community_buildings'))

        # Deleting field 'Machine.locationId'
        db.delete_column(u'laundry_machine', 'locationId')

        # Deleting field 'Machine.name'
        db.delete_column(u'laundry_machine', 'name')

        # Adding field 'Machine.numTotal'
        db.add_column(u'laundry_machine', 'numTotal',
                      self.gf('django.db.models.fields.IntegerField')(default=1, blank=True),
                      keep_default=False)

        # Adding field 'Machine.numAvail'
        db.add_column(u'laundry_machine', 'numAvail',
                      self.gf('django.db.models.fields.IntegerField')(default=1, blank=True),
                      keep_default=False)

        # Adding field 'Side.building'
        db.add_column(u'laundry_side', 'building',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laundry.Building'], null=True),
                      keep_default=False)

        # Adding field 'Building.community'
        db.add_column(u'laundry_building', 'community',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['laundry.Community'], null=True),
                      keep_default=False)

        # Removing M2M table for field sides on 'Building'
        db.delete_table(db.shorten_name(u'laundry_building_sides'))


    def backwards(self, orm):
        # Deleting model 'Washer'
        db.delete_table(u'laundry_washer')

        # Deleting model 'Dryer'
        db.delete_table(u'laundry_dryer')

        # Adding M2M table for field buildings on 'Community'
        m2m_table_name = db.shorten_name(u'laundry_community_buildings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('community', models.ForeignKey(orm[u'laundry.community'], null=False)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False))
        ))
        db.create_unique(m2m_table_name, ['community_id', 'building_id'])

        # Adding field 'Machine.locationId'
        db.add_column(u'laundry_machine', 'locationId',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'Machine.name'
        db.add_column(u'laundry_machine', 'name',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=40),
                      keep_default=False)

        # Deleting field 'Machine.numTotal'
        db.delete_column(u'laundry_machine', 'numTotal')

        # Deleting field 'Machine.numAvail'
        db.delete_column(u'laundry_machine', 'numAvail')

        # Deleting field 'Side.building'
        db.delete_column(u'laundry_side', 'building_id')

        # Deleting field 'Building.community'
        db.delete_column(u'laundry_building', 'community_id')

        # Adding M2M table for field sides on 'Building'
        m2m_table_name = db.shorten_name(u'laundry_building_sides')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False)),
            ('side', models.ForeignKey(orm[u'laundry.side'], null=False))
        ))
        db.create_unique(m2m_table_name, ['building_id', 'side_id'])


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
        u'laundry.dryer': {
            'Meta': {'object_name': 'Dryer', '_ormbases': [u'laundry.Machine']},
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Side']", 'null': 'True'}),
            u'machine_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['laundry.Machine']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'laundry.machine': {
            'Meta': {'object_name': 'Machine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numAvail': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'numTotal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'laundry.side': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Side'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Building']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.washer': {
            'Meta': {'object_name': 'Washer', '_ormbases': [u'laundry.Machine']},
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['laundry.Side']", 'null': 'True'}),
            u'machine_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['laundry.Machine']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['laundry']