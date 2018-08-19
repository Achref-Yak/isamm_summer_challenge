# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0014_auto_20180813_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_admin',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(max_length=7, default=''),
        ),
    ]
