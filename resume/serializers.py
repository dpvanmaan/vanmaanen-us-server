from django.forms import widgets
from rest_framework import serializers
from .models import Skill, SkillLevel, Experience, ExperienceCategory, Education, Course

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=('id','skill','exp_level')

class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=SkillLevel
        fields=('id','name','skills')
        dept=1
class ExperienceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ExperienceCategory
        fields=('id','name','jobs')
        depth=1
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields=('id','job_title','company','description','start','end','current',
                'location', 'order','category')
        depth=1

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields=('id','school','grad_date','degree','description','courses')
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields=('id','name','school')
