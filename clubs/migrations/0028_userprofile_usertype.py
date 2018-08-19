# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0027_userprofile_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
