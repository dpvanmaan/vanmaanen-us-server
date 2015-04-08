
from django.contrib import admin
from django.db import models
from django_markdown.admin import AdminMarkdownWidget
from .models import Post, Tag, Category, Comment, BlogImage
class BImageInline(admin.StackedInline):
    model = BlogImage
    extra = 1
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': AdminMarkdownWidget}}    
    inlines= [BImageInline]
admin.site.site_header="David vanMaanen Administration"
admin.site.site_title="David vanMaanen Admin"
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)

