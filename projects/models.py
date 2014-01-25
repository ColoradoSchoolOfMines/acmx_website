import datetime
from django.db import models
from django.utils import timezone

class Project(models.Model):
    project_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    team = models.ManyToManyField(UserProfile)
    pub_date = models.DateTimeField('date published', auto_now=True,
            auto_now_add=True)
    
    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    projects = models.ManyToManyField(Project)

    SEMESTER_CHOICES = (
            (SPRING, 'Spring'),
            (FALL, 'Fall'),
    )

    email = models.CharField(max_length=200)
    phone = models.CharField(_('Number'), maxlength = 40)
    homepage = models.URLFiels(max_length=200)
    major = models.CharField(max_length=200)
    grad_year = models.PositiveSmallIntegerField()
    grad_semester = models.CharField(max_length=10,
            choices=SEMESTER_CHOICES)

