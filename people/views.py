from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
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

    def get_queryset(self):
        return Staff.objects.get(user = self.request.user)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk = Staff.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = Student 
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return Student.objects.get(user = self.request.user)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk= Student.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class RecruiterViewset(viewsets.ModelViewSet):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return Recruiter.objects.get(user = self.request.user)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk= Recruiter.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)