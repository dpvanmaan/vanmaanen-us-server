from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import SkillSerializer, SkillLevelSerializer, ExperienceCategorySerializer,ExperienceSerializer, EducationSerializer, CourseSerializer
from .models import Skill, SkillLevel, Experience, ExperienceCategory, Education, Course
# Create your views here.
class SkillViewSet(viewsets.ModelViewSet):
    queryset= Skill.objects.all()
    serializer_class= SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class SkillLevelViewSet(viewsets.ModelViewSet):
    queryset= SkillLevel.objects.all()
    serializer_class= SkillLevelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset= Experience.objects.all()
    serializer_class= ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class ExperienceCategoryViewSet(viewsets.ModelViewSet):
    queryset= ExperienceCategory.objects.all()
    serializer_class= ExperienceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class EducationViewSet(viewsets.ModelViewSet):
    queryset= Education.objects.all()
    serializer_class= EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class CourseViewSet(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class= CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
