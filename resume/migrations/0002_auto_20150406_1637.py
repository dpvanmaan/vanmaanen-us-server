# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='ExpCategory',
            new_name='ExperienceCategory',
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RenameModel(
            old_name='ExpLevel',
            new_name='SkillLevel',
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='experiencecategory',
            options={'verbose_name_plural': 'Experience categories'},
        ),
    ]
