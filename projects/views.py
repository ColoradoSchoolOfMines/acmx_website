from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.views import generic
from django.utils import timezone

import markdown

from projects.models import Project, UserProfile


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['details'] = markdown.markdown(self.object.long_description,
                                               safe_mode='remove')
        return context

class IndexView(generic.list.ListView):
    model = Project
    template_name = 'projects/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProjectEditView(generic.edit.UpdateView):
    model = Project
    template_name = 'projects/project_edit.html'
    fields = ['title', 'description', 'long_description', 'link',
              'contributors', 'languages', 'image']

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
    fields = ['title', 'description', 'long_description', 'link',
              'contributors', 'languages', 'image']

    def get_success_url(self):
        # TODO: Is this safe?
        return reverse('projects:detail',
                       kwargs={'slug': slugify(self.request.POST['title'])})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)
