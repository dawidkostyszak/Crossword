from django.contrib import admin
from word.models import Question, Category, Word

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Word)
