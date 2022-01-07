from django.contrib.auth.models import User
from django.db.models import fields
from django.http import response
from rest_framework import serializers, validators
from drf_writable_nested.serializers import WritableNestedModelSerializer

from main.models import (
    File,
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
## helper function
def create_files(parent, obj, validated_data):
    request = obj.context.get("request")
    instance = parent().create(validated_data)
    files = request.FILES
    if files:
        for f in files.getlist("files"):
            instance.files.create(file=f)
    return instance     

## helper function
def update_files(parent, obj, instance, validated_data):
    request = obj.context.get("request")
    _ = parent().update(instance, validated_data)
    
    files = request.FILES
    
    if not obj.partial: ## when PUT request
        instance.files.clear()
    
    if files:
        for f in files.getlist("files"):
            instance.files.create(file=f)
    
    return instance

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, required = False)
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
    
    def create(self, validated_data):
        return create_files(super, self, validated_data)
    
    def update(self, instance, validated_data):
        return update_files(super, self, instance, validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, required = False)
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'addedBy':{'required':False},
            'tags':{'required':False},
            'students':{'required':False},
            'mentors':{'required':False},
        }

    def create(self, validated_data):
        return create_files(super, self, validated_data)
    
    def update(self, instance, validated_data):
        return update_files(super, self, instance, validated_data)

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

class StaffSerializer(WritableNestedModelSerializer):
    education = EducationSerializer(many = True)
    class Meta:
        model = Staff 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }
    
    def update(self, instance, validated_data):
        education = validated_data.pop('education')
        _ = super().update(instance, validated_data)
        
        if not self.partial: ## when PUT request
            instance.education.clear()
        
        for e in education:
            instance.education.add(
                Education.objects.get_or_create(
                    degree = e['degree'], 
                    year = e['year'], 
                    institution = e['institution']
                )[0]
            )
        return instance
        
class StudentSerializer(WritableNestedModelSerializer):
    education = EducationSerializer(many = True)
    class Meta:
        model = Student 
        fields = '__all__'
        extra_kwargs = {
            'user':{'required':False}
        }
    
    def update(self, instance, validated_data):
        education = validated_data.pop('education')
        _ = super().update(instance, validated_data)
        
        if not self.partial: ## when PUT request
            instance.education.clear()
        
        for e in education:
            instance.education.add(
                Education.objects.get_or_create(
                    degree = e['degree'], 
                    year = e['year'], 
                    institution = e['institution']
                )[0]
            )
        return instance
