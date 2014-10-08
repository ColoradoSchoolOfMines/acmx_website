# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20140920_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, default=1, auto_created=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
    ]
