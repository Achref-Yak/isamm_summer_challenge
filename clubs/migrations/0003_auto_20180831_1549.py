# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20180831_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='CoverImage',
            field=models.ImageField(upload_to='cover/', blank=True),
        ),
    ]
