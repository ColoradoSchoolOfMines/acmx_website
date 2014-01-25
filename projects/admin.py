from django.contrib import admin
from projects.models import Project
from projects.models import UserProfile

class ProjectAdmin(admin.ModelAdmin(:
    form = ProjectForm

    def __init__(self, model, admin_site):
        super(ProjectAdmin, self).__init__(model, admin_site)

admin.site.register(Project, ProjectAdmin)
admin.site.register(UserProfile)
