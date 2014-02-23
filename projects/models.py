import datetime
from django.db import models
from django.contrib.auth.models import User
from djangotoolbox import fields
from django.utils import timezone
import forms

class GenericListField(fields.ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, forms.StringListField, **kwargs)

class GenericDictField(fields.DictField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, forms.DictionaryField,
                **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=50)

    SEMESTER_CHOICES = (
            ('spring', 'Spring'),
            ('fall', 'Fall'),
    )

    name = models.CharField(max_length=75)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=40)
    homepage = models.URLField(max_length=200)
    major = models.CharField(max_length=200)
    grad_year = models.PositiveSmallIntegerField()
    grad_semester = models.CharField(max_length=10,
            choices=SEMESTER_CHOICES)
    stars = GenericListField()

    def __unicode__(self):
        return self.user.username

class Project(models.Model):
    project_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True,
            auto_now_add=True)
    team = GenericListField()
    main_image = models.CharField(max_length=200)
    pages = GenericDictField()
    tags = GenericListField()

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
