# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0013_auto_20180813_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='membre',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='club',
            field=models.ManyToManyField(to='clubs.Club', default=1),
        ),
    ]
