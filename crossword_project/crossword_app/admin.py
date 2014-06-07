from django.contrib import admin
from crossword_project.crossword_app.word.models import Question, Category, Word

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Word)
