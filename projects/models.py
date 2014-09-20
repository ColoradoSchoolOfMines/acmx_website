from django.db import models

class UserProfile(models.Model):
    pass

class Project(models.Model):
    project_id = models.SlugField(max_length=50, primary_key=True,
            unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    long_description = models.TextField()
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True,
            auto_now_add=True)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
