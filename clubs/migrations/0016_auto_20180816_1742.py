# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0015_auto_20180816_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_admin',
            field=models.OneToOneField(related_name='UserProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
