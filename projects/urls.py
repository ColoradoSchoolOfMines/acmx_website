from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^support$', views.SupportView.as_view(), name='support'),
    url(r'^p/(?P<pk>\w+)/$', views.DetailView.as_view(), name='detail'),
)
