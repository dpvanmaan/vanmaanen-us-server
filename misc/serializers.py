from rest_framework import serializers
from .models import Image, Text, Category
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=('name','pic','category')
        depth=1
class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model=Text
        fields=('name','body','text_type','category')
        depth=1
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name','images','texts')
        depth=1
