# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200, default='this is the description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='main_image',
            field=models.CharField(max_length=200, default='/no/image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2014, 8, 27), auto_now=True, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, default='Title'),
            preserve_default=False,
        ),
    ]
