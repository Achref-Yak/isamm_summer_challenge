# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0021_auto_20180817_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='club_admin',
        ),
        migrations.AddField(
            model_name='club',
            name='creater',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
