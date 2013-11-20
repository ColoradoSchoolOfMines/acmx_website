from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from acmxlabs.models import ACMXLabs


class IndexView(generic.ListView):
    template_name = 'acmxlabs/index.html'

class AboutView(generic.ListView):
    template_name = 'acmxlabs/about.html'

class SupportView(generic.ListView):
    template_name = 'acmxlabs/support.html'

def detail(request, project_id):
    p = get_object_or_404(ACMXLabs, pk=project_id)

