from django.conf.urls.defaults import patterns, include, url
# from app1.views import *
from offline_github.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$',home), 
	url(r'^offgit_login/$',offgit_login),
)
