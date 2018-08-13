# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom_de_club', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('site', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type_de_event', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('salle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('mission', models.TextField(default='', max_length=200)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin1',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
            options={
                'verbose_name_plural': 'SuperAdmin2',
            },
        ),
        migrations.AddField(
            model_name='etudiant',
            name='event',
            field=models.ForeignKey(default=1, to='clubs.Event'),
        ),
        migrations.AddField(
            model_name='admin',
            name='club',
            field=models.ForeignKey(to='clubs.Club'),
        ),
    ]
