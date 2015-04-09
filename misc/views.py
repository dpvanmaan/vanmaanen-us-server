from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from .models import Image, Text, Category
from .serializers import ImageSerializer, TextSerializer, CategorySerializer
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
class TextViewSet(viewsets.ModelViewSet):
    queryset=Text.objects.all()
    serializer_class=TextSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
class MiscCategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
