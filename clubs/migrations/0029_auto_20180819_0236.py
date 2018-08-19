# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0028_userprofile_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activity',
            field=models.ManyToManyField(default=1, blank=True, to='clubs.Activity'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(default='', blank=True, max_length=100),
        ),
    ]
