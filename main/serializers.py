from rest_framework import serializers

from django.contrib.auth.models import User

from main.models import Tag, Achievement, Project, Institution

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