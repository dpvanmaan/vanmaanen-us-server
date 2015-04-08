from django.forms import widgets
from rest_framework import serializers
from .models import Post, Tag, Category, Comment, BlogImage
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('first_name','last_name','email')

class PostSerializer(serializers.ModelSerializer):
    author=UserSerializer(many=False, read_only=True)
    class Meta:
        model= Post
        fields= ('id','title','abstract','body','created','category','tags','posted','author')
        depth=1
class PostMiniSerializer(serializers.ModelSerializer):
    author=UserSerializer(many=False, read_only=True)
    class Meta:
        model= Post
        fields= ('id','title','abstract','created','category','tags','posted','author')
        depth=1
class TagSerializer(serializers.ModelSerializer):
    posts=PostMiniSerializer(many=True, read_only=True)
    class Meta:
        model= Tag
        fields= ('id','name','posts')
class CategorySerializer(serializers.ModelSerializer):
    posts=PostMiniSerializer(many=True, read_only=True)
    class Meta:
        model= Category
        fields= ('id','name','posts')
class CommentSerializer(serializers.ModelSerializer):
    class Mepta:
        model= Comment
        fields= ('id','name','email','body','replyto','post','created')
class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= BlogImage
        fields= ('image_file','post')
