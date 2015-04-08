# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=255)),
                ('grad_date', models.DateField(null=True)),
                ('degree', models.CharField(max_length=500)),
                ('description', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=500)),
                ('description', models.TextField(default=b'')),
                ('start', models.DateField()),
                ('end', models.DateField(null=True)),
                ('current', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=500)),
                ('order', models.IntegerField()),
                ('category', models.ForeignKey(related_name='jobs', to='resume.ExpCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=255)),
                ('exp_level', models.ForeignKey(related_name='skills', to='resume.ExpLevel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='courses',
            name='school',
            field=models.ForeignKey(related_name='courses', to='resume.Education'),
            preserve_default=True,
        ),
    ]
