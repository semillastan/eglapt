# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'APT.added_by'
        db.alter_column('core_apt', 'added_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))


    def backwards(self, orm):
        
        # Changing field 'APT.added_by'
        db.alter_column('core_apt', 'added_by_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 25, 7, 54, 18, 192086)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 25, 7, 54, 18, 191992)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.apt': {
            'Meta': {'object_name': 'APT'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'added_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_added': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_played': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'game_level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.GameLevel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playing_time': ('django.db.models.fields.TimeField', [], {}),
            'total_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': "orm['auth.User']"})
        },
        'core.game': {
            'Meta': {'unique_together': "(('game_id', 'api_key'),)", 'object_name': 'Game'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'game_id': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'core.gamelevel': {
            'Meta': {'object_name': 'GameLevel'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'max_playing_time_unit': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'max_playing_time_value': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['core']
