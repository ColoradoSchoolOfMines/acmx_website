from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from projects.models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Project.objects.order_by('-pub_date')[:5]

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
        return get_object_or_404(Project, project_id=self.kwargs.get('pk'))

def detail(request, project_id):
    p = get_object_or_404(Project, project_id=project_id)
