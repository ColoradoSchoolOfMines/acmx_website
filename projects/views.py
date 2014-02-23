from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from projects.models import Project, UserProfile
from projects.modelforms import ProjectForm, UserProfileForm

# This is a temporary method, it will be removed later.
# Don't bother trying to improve it.
def welcome_message(user):
    if user.is_authenticated():
        return "Welcome, " + user.username + "!"
    return "Hi!"


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """Return all the things."""
        # FIXME: Once we get AJAX stuff, change this to return only a
        # subset of projects.
        return Project.objects.order_by('-pub_date') #[:5]

class AboutView(generic.TemplateView):
    template_name = 'projects/about.html'

    def get_context_data(self, **kwargs):
        return super(AboutView, self).get_context_data(**kwargs)

class ContactView(generic.TemplateView):
    template_name = 'projects/contact.html'

    def get_context_data(self, **kwargs):
        return super(ContactView, self).get_context_data(**kwargs)

class SupportView(generic.TemplateView):
    template_name = 'projects/support.html'

    def get_context_data(self, **kwargs):
        return super(SupportView, self).get_context_data(**kwargs)

class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_object(self, queryset=None):
        """Custom get_object override for our Mongo collection."""
        return get_object_or_404(Project,
                project_id=self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['welcome_message'] = welcome_message(self.request.user)
        return context

class ProjectListView(generic.ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.order_by('-pub_date')

class UserListView(generic.ListView):
    template_name = 'projects/user_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return UserProfile.objects.order_by('user')

class ProjectEditView(generic.edit.UpdateView):
    model = Project
    template_name = 'projects/project_edit.html'

    def get_object(self, queryset=None):
        """Custom get_object override for our Mongo collection."""
        return get_object_or_404(Project,
                project_id=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('projects:edit',
                kwargs={'pk': self.kwargs.get('pk')})

    # Make this view login-required.
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectEditView, self).dispatch(*args, **kwargs)

class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'projects/user_profile.html'

    def get_object(self, queryset=None):
        """Custom get_object override for our Mongo collection."""
        return get_object_or_404(UserProfile,
                username=self.kwargs.get('pk'))

class UserProfileEditView(generic.edit.UpdateView):
    model = UserProfile
    template_name = 'projects/user_profile_edit.html'

    def get_object(self, queryset=None):
        """Custom get_object override for our Mongo collection."""
        return get_object_or_404(UserProfile,
                username=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('projects:user_profile_edit',
                kwargs={'pk': self.kwargs.get('pk')})

    # Make this view login-required.
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileEditView, self).dispatch(*args, **kwargs)


def detail(request, project_id):
    p = get_object_or_404(Project, project_id=project_id)
