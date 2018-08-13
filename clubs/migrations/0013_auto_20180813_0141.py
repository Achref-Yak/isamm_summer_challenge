# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0012_auto_20180813_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='club',
        ),
        migrations.AddField(
            model_name='club',
            name='membre',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
