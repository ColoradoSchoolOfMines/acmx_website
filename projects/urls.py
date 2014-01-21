from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^support/$', views.SupportView.as_view(), name='support'),
    url(r'^project/(?P<pk>\w+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^admin/$', views.AdminView.as_view(), name="admin"),
#    url(r'^project/(?P<project_id>\d+)/$', views.DetailView.as_view(), name='detail'),

	# 404 reroute has to be last
	# url(r'^.*$', views.IndexView.as_view(), name='index'),	# return bad requests to the index page
)
