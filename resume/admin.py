from django.contrib import admin
from django_markdown.admin import AdminMarkdownWidget
from django.db import models
from .models import Skill, SkillLevel, Experience, ExperienceCategory, Education, Course
# Register your models here.
admin.site.register(Skill)
admin.site.register(SkillLevel)
admin.site.register(Experience)
admin.site.register(ExperienceCategory)
admin.site.register(Education)
admin.site.register(Course)
