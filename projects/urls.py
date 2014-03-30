from django.conf.urls import patterns, include, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
#    # Django built-in authentication
#    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':
#        'projects/login.html'}, name='login'),
    # Authentication from django-registration
    url(r'^accounts/', include('registration.backends.default.urls',
            namespace="registration")),
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^support$', views.SupportView.as_view(), name='support'),
    url(r'^p/$', views.ProjectListView.as_view(), name='project_list'),
    url(r'^p/(?P<pk>\w+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^p/(?P<pk>\w+)/edit$', views.ProjectEditView.as_view(), name='edit'),
    url(r'^p/new$', views.ProjectCreateView.as_view(), name='create'),
    url(r'^u/$', views.UserListView.as_view(), name='user_list'),
    url(r'^u/(?P<pk>\w+)/$', views.UserProfileView.as_view(),
        name='user_profile'),
    url(r'^u/(?P<pk>\w+)/edit$', views.UserProfileEditView.as_view(),
        name='user_profile_edit'),
)
