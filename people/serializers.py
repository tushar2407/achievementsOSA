from rest_framework import serializers
from people.models import (
    Education, 
    Recruiter,
    Skill, 
    Staff,
    Student, 
)

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education 
        fields = '__all__'

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill 
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }