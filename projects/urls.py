from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^support/$', views.SupportView.as_view(), name='support'),
    url(r'^project/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^project/(?P<project_id>\d+)/$', views.DetailView.as_view(), name='detail'),
)
