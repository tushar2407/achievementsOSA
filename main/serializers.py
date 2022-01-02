from rest_framework import serializers, validators

from django.contrib.auth.models import User

from main.models import (
    Tag,
    Achievement, 
    Project, 
    Institution,
    Skill,
    Education,
    Staff,
    Student,
    Recruiter
)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
        extra_kwargs = {
            'addedBy':{'required':False},
            'approvedBy':{'required':False},
            'teamMembers':{'required':False},
            'tags':{'required':False},
            'mentors':{'required':False},
        }

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'addedBy':{'required':False},
            'tags':{'required':False},
            'students':{'required':False},
            'mentors':{'required':False},
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name', 'last_name'
        )

class EducationSerializer(serializers.ModelSerializer):

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(EducationSerializer, self).run_validators(value)

    def create(self, validated_data):
        instance, _ = Education.objects.get_or_create(**validated_data)
        return instance

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
    education = EducationSerializer(many = True, read_only = True)
    class Meta:
        model = Staff 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }
        
class StudentSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many = True, read_only = True)
    class Meta:
        model = Student 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }