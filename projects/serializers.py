from rest_framework import serializers
from .models import Project, Link, Tag, Screenshot
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('title','tags','description','icon','links','screens')
        depth=1
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields=('title','url','project')
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=('name','projects')
class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Screenshot
        fields=('title','image','project')


