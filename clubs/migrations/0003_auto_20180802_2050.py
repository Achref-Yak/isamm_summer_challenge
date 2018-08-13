# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20180802_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='club',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='event',
        ),
    ]
