# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Difficulty'
        db.create_table(u'word_difficulty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('difficulty', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'word', ['Difficulty'])

        # Adding model 'Question'
        db.create_table(u'word_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(max_length=150)),
            ('difficulty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['word.Difficulty'])),
        ))
        db.send_create_signal(u'word', ['Question'])

        # Adding model 'Word'
        db.create_table(u'word_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['word.Question'])),
        ))
        db.send_create_signal(u'word', ['Word'])


    def backwards(self, orm):
        # Deleting model 'Difficulty'
        db.delete_table(u'word_difficulty')

        # Deleting model 'Question'
        db.delete_table(u'word_question')

        # Deleting model 'Word'
        db.delete_table(u'word_word')


    models = {
        u'word.difficulty': {
            'Meta': {'object_name': 'Difficulty'},
            'difficulty': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'word.question': {
            'Meta': {'object_name': 'Question'},
            'difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['word.Difficulty']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '150'})
        },
        u'word.word': {
            'Meta': {'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['word.Question']"})
        }
    }

    complete_apps = ['word']