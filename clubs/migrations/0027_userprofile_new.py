# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0026_auto_20180818_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
