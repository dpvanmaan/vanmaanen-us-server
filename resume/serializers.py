from django.forms import widgets
from rest_framework import serializers
from .models import Skill, SkillLevel, Experience, ExperienceCategory, Education, Course

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=('id','skill','exp_level')
        depth=1
class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=SkillLevel
        fields=('id','name','skills')
        depth=2
class ExperienceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ExperienceCategory
        fields=('id','name','jobs')
        depth=2
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields=('id','job_title','company','description','start','end','current',
                'location', 'order','category')
        depth=1

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields=('id','school','grad_date','degree','description','courses')
        depth=2
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('id','name','school')
        depth=1
