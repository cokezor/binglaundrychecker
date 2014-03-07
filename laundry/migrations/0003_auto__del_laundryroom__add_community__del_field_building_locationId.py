# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LaundryRoom'
        db.delete_table(u'laundry_laundryroom')

        # Removing M2M table for field machines on 'LaundryRoom'
        db.delete_table(db.shorten_name(u'laundry_laundryroom_machines'))

        # Adding model 'Community'
        db.create_table(u'laundry_community', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('locationId', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'laundry', ['Community'])

        # Adding M2M table for field laundryRooms on 'Community'
        m2m_table_name = db.shorten_name(u'laundry_community_laundryRooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('community', models.ForeignKey(orm[u'laundry.community'], null=False)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False))
        ))
        db.create_unique(m2m_table_name, ['community_id', 'building_id'])

        # Deleting field 'Building.locationId'
        db.delete_column(u'laundry_building', 'locationId')

        # Removing M2M table for field laundryRooms on 'Building'
        db.delete_table(db.shorten_name(u'laundry_building_laundryRooms'))

        # Adding M2M table for field machines on 'Building'
        m2m_table_name = db.shorten_name(u'laundry_building_machines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False)),
            ('machine', models.ForeignKey(orm[u'laundry.machine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['building_id', 'machine_id'])


    def backwards(self, orm):
        # Adding model 'LaundryRoom'
        db.create_table(u'laundry_laundryroom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'laundry', ['LaundryRoom'])

        # Adding M2M table for field machines on 'LaundryRoom'
        m2m_table_name = db.shorten_name(u'laundry_laundryroom_machines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('laundryroom', models.ForeignKey(orm[u'laundry.laundryroom'], null=False)),
            ('machine', models.ForeignKey(orm[u'laundry.machine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['laundryroom_id', 'machine_id'])

        # Deleting model 'Community'
        db.delete_table(u'laundry_community')

        # Removing M2M table for field laundryRooms on 'Community'
        db.delete_table(db.shorten_name(u'laundry_community_laundryRooms'))

        # Adding field 'Building.locationId'
        db.add_column(u'laundry_building', 'locationId',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding M2M table for field laundryRooms on 'Building'
        m2m_table_name = db.shorten_name(u'laundry_building_laundryRooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False)),
            ('laundryroom', models.ForeignKey(orm[u'laundry.laundryroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['building_id', 'laundryroom_id'])

        # Removing M2M table for field machines on 'Building'
        db.delete_table(db.shorten_name(u'laundry_building_machines'))


    models = {
        u'laundry.building': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.Machine']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.community': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laundryRooms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.Building']", 'symmetrical': 'False'}),
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