from django.contrib import admin
from projects.models import Project
from projects.models import UserProfile

admin.site.register(Project)
admin.site.register(UserProfile)
