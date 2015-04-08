# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'blog/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('Comment', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=500)),
                ('body', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=500, null=True)),
                ('abstract', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now=True)),
                ('posted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='blogs', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(related_name='posts', to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', null=True, to='blog.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='blog.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='replyto',
            field=models.ForeignKey(related_name='replies', to='blog.Comment', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogimage',
            name='post',
            field=models.ForeignKey(related_name='images', to='blog.Post'),
            preserve_default=True,
        ),
    ]
