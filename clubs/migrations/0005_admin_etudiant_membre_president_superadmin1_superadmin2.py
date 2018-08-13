# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20180807_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin1',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=30)),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
            options={
                'verbose_name_plural': 'SuperAdmin2',
            },
        ),
    ]
