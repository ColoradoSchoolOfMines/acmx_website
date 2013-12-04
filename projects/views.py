from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from projects.models import Projects


class IndexView(generic.ListView):
    template_name = 'projects/index.html'

class AboutView(generic.ListView):
    template_name = 'projects/about.html'

class SupportView(generic.ListView):
    template_name = 'projects/support.html'

def detail(request, project_id):
    p = get_object_or_404(Projects, pk=project_id)

