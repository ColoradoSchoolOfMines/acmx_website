# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_contributors'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.CharField(max_length=200, default='None'),
            preserve_default=False,
        ),
    ]
