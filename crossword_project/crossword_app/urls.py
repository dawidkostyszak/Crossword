from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import HomepageView, CrosswordGenerate

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crossword_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name="home"),
    url(r'^crossword/', CrosswordGenerate.as_view(), name="crossword"),
    (r'^accounts/', include('crossword_app.auth.urls', app_name='authorization')),
    (r'^word/', include('crossword_app.word.urls', app_name='word')),
)
