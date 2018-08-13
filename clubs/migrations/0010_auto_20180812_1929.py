# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0009_auto_20180811_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='club',
        ),
        migrations.AddField(
            model_name='club',
            name='membre',
            field=models.ForeignKey(to='clubs.UserProfile', default=1),
        ),
        migrations.DeleteModel(
            name='Membre',
        ),
    ]
