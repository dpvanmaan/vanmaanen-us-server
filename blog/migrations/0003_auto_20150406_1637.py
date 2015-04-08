# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150403_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 16, 37, 39, 893105, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
