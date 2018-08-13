# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20180808_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='city',
            new_name='niveau',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='site',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone',
            new_name='tel',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
