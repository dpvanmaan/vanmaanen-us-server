# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Comment',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Note', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
