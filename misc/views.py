from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters
from .models import Image, Text, Category, File
from .serializers import ImageSerializer, TextSerializer, CategorySerializer, FileSerializer
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category__name','name')
    queryset=Image.objects.all()
    serializer_class=ImageSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
class TextViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category__name','name')
    queryset=Text.objects.all()
    serializer_class=TextSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
class MiscCategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticatedOrReadOnly] 
class FileViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category__name','name')
    queryset=File.objects.all()
    serializer_class=FileSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
