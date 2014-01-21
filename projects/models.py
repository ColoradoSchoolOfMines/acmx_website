import datetime
from mongoengine import *
from django.utils import timezone

class Project(Document):
    project_id = StringField(max_length=25)
    title = StringField(max_length=200)
    description = StringField(max_length=200)
    pub_date = DateTimeField('date published')
    
    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
