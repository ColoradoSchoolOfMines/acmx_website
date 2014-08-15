from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('projects.urls', namespace='projects')),
    url(r'^admin/', include(admin.site.urls)),
)
