# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20140920_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='main_image',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='long_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
