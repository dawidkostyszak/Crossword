from django.conf.urls import patterns, url
from django.contrib import admin
from views import WordAdd, WordsList, Words

admin.autodiscover()

urlpatterns = patterns('crossword_app.word.views',
    url(r'^$', Words.as_view(), name="words"),
    url(r'^add/$', WordAdd.as_view(), name='add_word'),
    url(r'^list/$', WordsList.as_view(), name='words_list')
)
