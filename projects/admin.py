from django.contrib import admin
from .models import Project, Link, Tag, Screenshot
from django_markdown.admin import AdminMarkdownWidget
from django.db import models

class LinkInline(admin.StackedInline):
    model= Link
    extra=1
class ScreenInline(admin.StackedInline):
    model= Screenshot
    extra=1
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrirdes= {models.TextField:  {'widget': AdminMarkdownWidget}}
    inlines=[LinkInline,ScreenInline]
    

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
