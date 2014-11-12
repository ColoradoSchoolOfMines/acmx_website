from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from projects import views

urlpatterns = patterns('',
    # Template views.
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    #url(r'^$', TemplateView.as_view(template_name='projects/index.html'),
     #   name='index'),
    url(r'^about$', TemplateView.as_view(template_name='projects/about.html'),
        name='about'),
    url(r'^contact$', TemplateView.as_view(template_name='projects/contact.html'),
        name='contact'),
    # Project views.
    url(r'^p/(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^p/(?P<slug>[\w-]+)/edit$', views.ProjectEditView.as_view(), name='edit'),
    url(r'^p/new$', views.ProjectCreateView.as_view(), name='create'),
)