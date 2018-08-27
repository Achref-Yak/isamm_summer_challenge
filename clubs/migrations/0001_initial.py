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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom_de_event', models.CharField(max_length=30, default='')),
                ('info', models.CharField(max_length=1000, default='')),
                ('date', models.DateField(verbose_name='Date', default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom_de_club', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('site', models.CharField(max_length=30)),
                ('superviseur', models.ForeignKey(related_name='superviseur', default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='demander',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user_from_name', models.CharField(max_length=35, default=1)),
                ('accepted', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('invi_type', models.CharField(max_length=20, default='')),
                ('club', models.ForeignKey(to='clubs.Club', default=1)),
                ('user_from', models.ForeignKey(related_name='user_from', default=1, to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(related_name='user_to', default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, default='')),
                ('password', models.CharField(max_length=50, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom_de_event', models.CharField(max_length=50, default='')),
                ('type_de_event', models.CharField(max_length=50, default='')),
                ('description', models.CharField(max_length=200, default='')),
                ('date', models.DateField()),
                ('salle', models.CharField(max_length=20, default='')),
                ('recompenses', models.CharField(max_length=20, default='')),
                ('partenaires', models.CharField(max_length=20, default='')),
                ('sponsors', models.CharField(max_length=20, default='')),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
                ('club', models.ForeignKey(to='clubs.Club', default=1)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('niveau', models.CharField(max_length=100, default='')),
                ('skills', models.CharField(max_length=100, default='')),
                ('site', models.CharField(max_length=100, default='')),
                ('tel', models.IntegerField(default=0)),
                ('user_type', models.CharField(max_length=7, default='')),
                ('image', models.ImageField(upload_to='profile/', default='profile/default-user.png')),
                ('new', models.BooleanField(default=True)),
                ('usertype', models.CharField(blank=True, max_length=100, default='')),
                ('club', models.ManyToManyField(to='clubs.Club', default=1)),
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
            field=models.ForeignKey(to='clubs.Event', default=1),
        ),
        migrations.AddField(
            model_name='activity',
            name='nom_de_club',
            field=models.ForeignKey(default=1, blank=True, to='clubs.Club'),
        ),
    ]
