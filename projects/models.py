from django.db import models

class UserProfile(models.Model):
    pass

class Project(models.Model):
    project_id = models.SlugField(max_length=50, primary_key=True,
            unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True,
            auto_now_add=True)
    main_image = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def epoch(self):
        return int(self.pub_date.strftime("%s"))

    def short_desc(self):
        return self.description if len(self.description) <= 38 else ' '.join(self.description[:38].split(' ')[:-1]) + '...'

    def html_pages(self):
        return { k: markdown(v, safe_mode='escape') for k, v in self.pages.iteritems() }

    def other_pages(self):
        return { slugify(k): (k, v) for k, v in self.html_pages().iteritems() if k != 'Description' }

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
