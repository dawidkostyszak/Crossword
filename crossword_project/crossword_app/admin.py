from django.contrib import admin
from word.models import Question, Difficulty, Word

admin.site.register(Question)
admin.site.register(Difficulty)
admin.site.register(Word)
