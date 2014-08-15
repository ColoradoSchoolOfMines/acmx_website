from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from projects.models import Project, UserProfile


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'


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

    def get_success_url(self):
        return reverse('projects:edit',
                       kwargs={'pk': self.kwargs.get('pk')})


class ProjectCreateView(generic.edit.CreateView):
    model = Project
    template_name = 'projects/project_create.html'

    def get_success_url(self):
        # TODO: Is this safe?
        return reverse('projects:detail',
                       kwargs={'pk': self.request.POST['project_id']})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)


class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'projects/user_profile.html'


class UserProfileEditView(generic.edit.UpdateView):
    model = UserProfile
    template_name = 'projects/user_profile_edit.html'

    def get_success_url(self):
        return reverse('projects:user_profile_edit',
                       kwargs={'pk': self.kwargs.get('pk')})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileEditView, self).dispatch(*args, **kwargs)
