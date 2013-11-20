from django.conf.urls import patterns, url
from acmxlabs import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^support/$', views.SupportView.as_view(), name='support'),
    url(r'^project/(?P<project_id>\d+)/$', views.details, name='details'),
)
