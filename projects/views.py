from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.views import generic

from projects.models import Project, UserProfile


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project.html'


class ProjectEditView(generic.edit.UpdateView):
    model = Project
    template_name = 'projects/project_edit.html'
    fields = ['title', 'description', 'long_description', 'link']

    def get_success_url(self):
        # TODO: Is this safe?
        return reverse('projects:detail',
                       kwargs={'slug': slugify(self.request.POST['title'])})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectEditView, self).dispatch(*args, **kwargs)


class ProjectCreateView(generic.edit.CreateView):
    model = Project
    template_name = 'projects/project_create.html'
    fields = ['title', 'description', 'long_description', 'link']

    def get_success_url(self):
        # TODO: Is this safe?
        return reverse('projects:detail',
                       kwargs={'slug': slugify(self.request.POST['title'])})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)
