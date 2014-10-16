# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
    ]
