from django.shortcuts import render
from people.models import (
    Department, 
    Education,
    Recruiter,
    Skill,
    Staff, 
    Student
)
from people.serializers import (
    DepartmentSerializer, 
    EducationSerializer,
    RecruiterSerializer,
    SkillSerializer,
    StaffSerializer, 
    StudentSerializer

)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class EducationViewset(viewsets.ModelViewSet):
    serializer_class = EducationSerializer 
    queryset = Education.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class SkillViewset(viewsets.ModelViewSet):
    serializer_class = SkillSerializer 
    queryset = Skill.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class StaffViewset(viewsets.ModelViewSet):
    serializer_class = StaffSerializer 
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = Student 
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]