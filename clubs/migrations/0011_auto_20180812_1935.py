# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0010_auto_20180812_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='membre',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='club',
            field=models.ForeignKey(to='clubs.Club', default=1),
        ),
    ]
