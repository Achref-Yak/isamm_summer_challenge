# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0019_auto_20180817_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='invitation',
        ),
        migrations.AddField(
            model_name='club',
            name='invitation',
            field=models.ForeignKey(default=1, to='clubs.Invitation'),
        ),
    ]
