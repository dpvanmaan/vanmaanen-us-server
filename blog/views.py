from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import PostSerializer, TagSerializer, CategorySerializer, CommentSerializer, BlogImageSerializer, UserSerializer, PostMiniSerializer
from .models import Post, Tag, Category, Comment, BlogImage
from django.contrib.auth.models import User
# Create your views here.
class PostPubViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(posted=True)
    def list(self, request):
        tag_name=request.QUERY_PARAMS.get('tag',None)
        cat_name=request.QUERY_PARAMS.get('cat',None)
        queryset=self.queryset
        if tag_name is not None:
            queryset = queryset.filter(tags__name=tag_name)
        if cat_name is not None:
            queryset = queryset.filter(category__name=cat_name)
        serializer_class=PostMiniSerializer
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer=serializer_class(queryset, many=True)
        return Response(serializer.data)
class PostPrivViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    def list(self, request):
        tag_name=request.QUERY_PARAMS.get('tag',None)
        cat_name=request.QUERY_PARAMS.get('cat',None)
        queryset=self.queryset
        if tag_name is not None:
            queryset = queryset.filter(tags__name=tag_name)
        if cat_name is not None:
            queryset = queryset.filter(category__name=cat_name)
        serializer_class=PostMiniSerializer
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer=serializer_class(queryset, many=True)
        return Response(serializer.data)
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Tag.objects.all()
        tag_name=self.request.QUERY_PARAMS.get('name',None)
        if tag_name is not None:
            queryset = queryset.filter(name=tag_name)
        return queryset
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class BlogImageViewSet(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
