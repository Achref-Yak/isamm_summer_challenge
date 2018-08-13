# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0003_auto_20180802_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=100, default='')),
                ('city', models.CharField(max_length=100, default='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='club',
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
        migrations.RemoveField(
            model_name='membre',
            name='club',
        ),
        migrations.RemoveField(
            model_name='president',
            name='club',
        ),
        migrations.RemoveField(
            model_name='superadmin1',
            name='club',
        ),
        migrations.RemoveField(
            model_name='superadmin2',
            name='club',
        ),
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.DeleteModel(
            name='Membre',
        ),
        migrations.DeleteModel(
            name='President',
        ),
        migrations.DeleteModel(
            name='SuperAdmin1',
        ),
        migrations.DeleteModel(
            name='SuperAdmin2',
        ),
    ]
