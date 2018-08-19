# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0020_auto_20180817_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='invitation',
        ),
        migrations.AddField(
            model_name='club',
            name='invitation',
            field=models.ManyToManyField(to='clubs.Invitation'),
        ),
    ]
