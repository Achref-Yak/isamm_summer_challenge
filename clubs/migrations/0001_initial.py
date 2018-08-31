# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom_de_event', models.CharField(default='', max_length=30)),
                ('info', models.CharField(default='', max_length=1000, blank=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('image', models.ImageField(default=None, upload_to='pics/', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom_de_club', models.CharField(max_length=30)),
                ('description', models.CharField(default='', max_length=1000)),
                ('email', models.CharField(default='', max_length=30)),
                ('site', models.CharField(default='', max_length=30)),
                ('CoverImage', models.ImageField(default=None, upload_to='pics/', blank=True)),
                ('superviseur', models.ForeignKey(default=1, related_name='superviseur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='demander',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('user_from_name', models.CharField(default=1, max_length=35)),
                ('accepted', models.BooleanField(default=False)),
                ('invi_type', models.CharField(default='', max_length=20)),
                ('club', models.ForeignKey(default=1, to='clubs.Club')),
                ('user_from', models.ForeignKey(default=1, related_name='user_from', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(default=1, related_name='user_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom_de_event', models.CharField(default='', max_length=50)),
                ('type_de_event', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
                ('date', models.DateField()),
                ('salle', models.CharField(default='', max_length=20)),
                ('recompenses', models.CharField(default='', max_length=20)),
                ('partenaires', models.CharField(default='', max_length=20)),
                ('sponsors', models.CharField(default='', max_length=20)),
                ('admin', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('club', models.ForeignKey(default=1, to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('info', models.CharField(default=1, max_length=65)),
                ('seen', models.BooleanField(default=False)),
                ('club', models.ForeignKey(default=1, related_name='club_to_notification', to='clubs.Club')),
                ('user_from', models.ForeignKey(default=1, related_name='user_from_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin1',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
            options={
                'verbose_name_plural': 'SuperAdmin1',
            },
        ),
        migrations.CreateModel(
            name='SuperAdmin2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
            options={
                'verbose_name_plural': 'SuperAdmin2',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('niveau', models.CharField(default='', max_length=100)),
                ('skills', models.CharField(default='', max_length=100)),
                ('site', models.CharField(default='', max_length=100)),
                ('tel', models.IntegerField(default=0)),
                ('user_type', models.CharField(default='', max_length=7)),
                ('image', models.ImageField(default='profile/default-user.png', upload_to='profile/')),
                ('new', models.BooleanField(default=True)),
                ('usertype', models.CharField(default='', max_length=100, blank=True)),
                ('club', models.ManyToManyField(default=1, to='clubs.Club')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='admin',
            name='club',
            field=models.ForeignKey(to='clubs.Club'),
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(default=1, to='clubs.Event'),
        ),
        migrations.AddField(
            model_name='activity',
            name='nom_de_club',
            field=models.ForeignKey(default=1, to='clubs.Club', blank=True),
        ),
    ]
