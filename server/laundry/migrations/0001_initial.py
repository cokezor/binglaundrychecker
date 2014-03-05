# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Machine'
        db.create_table(u'laundry_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'laundry', ['Machine'])

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

        # Adding model 'Building'
        db.create_table(u'laundry_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'laundry', ['Building'])

        # Adding M2M table for field laundryRooms on 'Building'
        m2m_table_name = db.shorten_name(u'laundry_building_laundryRooms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('building', models.ForeignKey(orm[u'laundry.building'], null=False)),
            ('laundryroom', models.ForeignKey(orm[u'laundry.laundryroom'], null=False))
        ))
        db.create_unique(m2m_table_name, ['building_id', 'laundryroom_id'])


    def backwards(self, orm):
        # Deleting model 'Machine'
        db.delete_table(u'laundry_machine')

        # Deleting model 'LaundryRoom'
        db.delete_table(u'laundry_laundryroom')

        # Removing M2M table for field machines on 'LaundryRoom'
        db.delete_table(db.shorten_name(u'laundry_laundryroom_machines'))

        # Deleting model 'Building'
        db.delete_table(u'laundry_building')

        # Removing M2M table for field laundryRooms on 'Building'
        db.delete_table(db.shorten_name(u'laundry_building_laundryRooms'))


    models = {
        u'laundry.building': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laundryRooms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.LaundryRoom']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.laundryroom': {
            'Meta': {'ordering': "('name',)", 'object_name': 'LaundryRoom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['laundry.Machine']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'laundry.machine': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Machine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['laundry']