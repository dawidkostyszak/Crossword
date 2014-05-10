from django.conf.urls import patterns, url
from django.contrib import admin
from views import WordAdd, WordList

admin.autodiscover()

urlpatterns = patterns('crossword_app.word.views',
    url(r'^$', WordList.as_view(), name="words_list"),
    url(r'^add/$', WordAdd.as_view(), name='add_word'),
)
