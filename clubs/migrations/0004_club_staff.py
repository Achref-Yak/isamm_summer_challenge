# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0003_auto_20180831_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='staff',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, default=1),
        ),
    ]
