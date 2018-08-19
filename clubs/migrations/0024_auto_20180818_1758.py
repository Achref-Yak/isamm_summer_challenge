# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0023_auto_20180818_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='superadmin',
            new_name='superviseur',
        ),
    ]
