# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Side.washerTimes'
        db.alter_column(u'laundry_side', 'washerTimes', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=20, null=True))

        # Changing field 'Side.dryerTotal'
        db.alter_column(u'laundry_side', 'dryerTotal', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Side.dryerAvail'
        db.alter_column(u'laundry_side', 'dryerAvail', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Side.washerAvail'
        db.alter_column(u'laundry_side', 'washerAvail', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Side.washerInUse'
        db.alter_column(u'laundry_side', 'washerInUse', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Side.washerTotal'
        db.alter_column(u'laundry_side', 'washerTotal', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Side.dryerTimes'
        db.alter_column(u'laundry_side', 'dryerTimes', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=20, null=True))

        # Changing field 'Side.dryerInUse'
        db.alter_column(u'laundry_side', 'dryerInUse', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Side.washerTimes'
        raise RuntimeError("Cannot reverse this migration. 'Side.washerTimes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.washerTimes'
        db.alter_column(u'laundry_side', 'washerTimes', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Side.dryerTotal'
        raise RuntimeError("Cannot reverse this migration. 'Side.dryerTotal' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.dryerTotal'
        db.alter_column(u'laundry_side', 'dryerTotal', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Side.dryerAvail'
        raise RuntimeError("Cannot reverse this migration. 'Side.dryerAvail' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.dryerAvail'
        db.alter_column(u'laundry_side', 'dryerAvail', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Side.washerAvail'
        raise RuntimeError("Cannot reverse this migration. 'Side.washerAvail' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.washerAvail'
        db.alter_column(u'laundry_side', 'washerAvail', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Side.washerInUse'
        raise RuntimeError("Cannot reverse this migration. 'Side.washerInUse' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.washerInUse'
        db.alter_column(u'laundry_side', 'washerInUse', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Side.washerTotal'
        raise RuntimeError("Cannot reverse this migration. 'Side.washerTotal' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.washerTotal'
        db.alter_column(u'laundry_side', 'washerTotal', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Side.dryerTimes'
        raise RuntimeError("Cannot reverse this migration. 'Side.dryerTimes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.dryerTimes'
        db.alter_column(u'laundry_side', 'dryerTimes', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Side.dryerInUse'
        raise RuntimeError("Cannot reverse this migration. 'Side.dryerInUse' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Side.dryerInUse'
        db.alter_column(u'laundry_side', 'dryerInUse', self.gf('django.db.models.fields.IntegerField')())

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
            'dryerAvail': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dryerInUse': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dryerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20', 'null': 'True'}),
            'dryerTotal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationId': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'washerAvail': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'washerInUse': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'washerTimes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20', 'null': 'True'}),
            'washerTotal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['laundry']