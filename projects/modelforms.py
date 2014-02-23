from django.forms import ModelForm
from projects.models import Project, UserProfile

class ProjectForm(ModelForm):
    class Meta:
        model = Project

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
