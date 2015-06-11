from django.contrib import admin
from .models import Image, Text, Category, File
# Register your models here.

admin.site.register(Image)
admin.site.register(Text)
admin.site.register(Category)
admin.site.register(File)
