# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20140920_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
