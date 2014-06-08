from django.conf.urls import patterns, url
from django.contrib import admin
from views import LoginView, LogoutView

admin.autodiscover()

urlpatterns = patterns('crossword_app.auth.views',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout')
)
