# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_auto_20180812_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='club',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='club',
            field=models.ManyToManyField(to='clubs.Club', default=1),
        ),
    ]
