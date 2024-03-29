from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.files import File as django_File
from django.core.files.storage import default_storage
from django.db.models import Q
from django.http import request, response
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication 
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authenticate.decorators import is_admin
from authenticate.models import Profile
from authenticate.serializers import ProfileSerializer
from main.models import (
    Banner,
    Tag, 
    Project, 
    Achievement, 
    Institution,
    Skill,
    Education,
    Staff,
    Student,
    Recruiter,
    File,
    CATEGORY_CHOICES,
)
from main.serializers import (
    BannerSerializer,
    FileSerializer,
    TagSerializer, 
    ProjectSerializer, 
    AchievementSerializer, 
    InstitutionSerializer,
    UserSerializer,
    EducationSerializer,
    RecruiterSerializer,
    SkillSerializer,
    StaffSerializer, 
    StudentSerializer,
)
from main.utils import get_achievements_json_format, get_projects_json_format

from datetime import datetime 
import json
import os
# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class InstitutionViewset(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def retrieve(self, request, pk, *args, **kwargs):
        i = self.serializer_class(get_object_or_404(Project, id = pk)).data
        
        u = User.objects.get(id = i['addedBy'])
        i['addedBy'] =  UserSerializer(u).data
    
        if i['approvedBy']:
            i['approvedBy'] = StaffSerializer(Staff.objects.get(id = i['approvedBy'])).data        
        
        if i['institution']:
            i['institution'] = InstitutionSerializer(Institution.objects.get(id = i['institution'])).data        
        
        if i['tags']:
            i['tags'] = TagSerializer(Tag.objects.filter(id__in = i['tags']), many=True).data
    
        if i['mentors']:
            i['mentors'] =  StaffSerializer(Staff.objects.filter(id__in = i['mentors']), many=True).data
    
        if i['students']:
            i['students'] = StudentSerializer(Student.objects.filter(id__in = i['teamMembers']), many=True).data
        
        return JsonResponse(i)
    
    def list(self, *args, **kwargs):
        return JsonResponse({'projects' : get_projects_json_format(self.request.user)})
    
    # def partial_update(self, request, pk, *args, **kwargs):
    #     pk= request.user.id
    #     return super().partial_update(request, pk, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(addedBy = self.request.user)

class AchievementViewset(viewsets.ModelViewSet):
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def retrieve(self, request, pk, *args, **kwargs):
        i = self.serializer_class(get_object_or_404(Achievement, id = pk)).data

        u = User.objects.get(id = i['addedBy'])
        i['addedBy'] = UserSerializer(u).data
        # i['addedBy'] = ProfileSerializer(Profile.objects.get(user=u)).data
    
        if i['approvedBy']:
            i['approvedBy'] = StaffSerializer(Staff.objects.get(id = i['approvedBy'])).data        
        
        if i['institution']:
            i['institution'] = InstitutionSerializer(Institution.objects.get(id = i['institution'])).data        
        
        if i['tags']:
            i['tags'] = TagSerializer(Tag.objects.filter(id__in = i['tags']), many=True).data
    
        if i['mentors']:
            i['mentors'] = StaffSerializer(Staff.objects.filter(id__in = i['mentors']), many=True).data
    
        if i['teamMembers']:
            i['teamMembers'] = UserSerializer(User.objects.filter(id__in = i['teamMembers']), many=True).data

        return JsonResponse(i)

    def list(self, *args, **kwargs):
        return JsonResponse({'achievements' : get_achievements_json_format(self.request.user)})

    # def partial_update(self, request, pk, *args, **kwargs):
    #     pk= request.user.id
    #     return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(addedBy = self.request.user)

class EducationViewset(viewsets.ModelViewSet):
    serializer_class = EducationSerializer 
    queryset = Education.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return self.queryset.distinct('degree')

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
        return self.queryset.filter(user = self.request.user)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk = Staff.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        r  = Response(data = self.serializer_class(Staff.objects.get(user=user)).data)
        r.data['name'] = user.first_name+ " " + user.last_name
        r.data['username'] = user.username
        r.data['email'] = user.email
        return r

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer 
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk= Student.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        r  = Response(data = self.serializer_class(Student.objects.get(user=user)).data)
        r.data['name'] = user.first_name+ " " + user.last_name
        r.data['username'] = user.username
        r.data['email'] = user.email
        return r

class RecruiterViewset(viewsets.ModelViewSet):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk= Recruiter.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class FileViewset(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class BannerViewset(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_authenticators(self):
        if self.request.method == 'GET':
            authentication_classes = []
        else:
            authentication_classes = [TokenAuthentication]
        return [auth() for auth in authentication_classes]

def homepage(request):
    achievements_students = AchievementSerializer(Achievement.objects.filter(addedBy__profile__designation = 1).order_by('-dateCreated')[:10], many=True).data
    achievements_staffs = AchievementSerializer(Achievement.objects.filter(addedBy__profile__designation = 2).order_by('-dateCreated')[:10], many=True).data
    publication_tags = Tag.objects.filter(Q(title__contains = 'paper') | Q(title__contains = 'publication'))
    publications = AchievementSerializer(Achievement.objects.filter(tags__in = list(publication_tags)).order_by('-dateCreated')[:10], many=True).data

    return JsonResponse({
            'student_achievements' : achievements_students,
            'staff_achievements' : achievements_staffs,
            'publications' : publications
        },
        status = status.HTTP_200_OK
    )

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
@authentication_classes([TokenAuthentication,])
def get_professors(request):
    professors =  list(Staff.objects.all().values('user__email', 'id'))
    return JsonResponse(
        {
            'professors': professors
        }
    )

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
@authentication_classes([TokenAuthentication,])
def get_students(request):
    students = list(Student.objects.all().values('user__email', 'user__id'))
    return JsonResponse(
        {
            'students': students
        }
    )

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
@authentication_classes([TokenAuthentication,])
def get_achievements_admin(request):
    if Profile.objects.get(user = request.user).is_admin():
        unapproved = list(Achievement.objects.filter(approved = "Pending").values())
        
        return JsonResponse(
            {
                'unapproved': unapproved
            }
        )
    return JsonResponse(
        {
            'details': 'Not an admin'
        }
    )

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
@authentication_classes([TokenAuthentication,])
def get_projects_admin(request):
    if Profile.objects.get(user = request.user).is_admin():
        unapproved = list(Project.objects.filter(approved = "Pending").values())
        
        return JsonResponse(
            {
                'unapproved': unapproved
            }
        )
    return JsonResponse(
        {
            'details': 'Not an admin'
        }
    )

def search(request):
    query = request.GET['q']
    achievements = list(Achievement.objects.filter(title__icontains = query).values())
    projects = list(Project.objects.filter(title__icontains = query).values())

    return JsonResponse({
        'achievements' : achievements,
        'projects' : projects,
    })

def get_graph_data(request):
    achievements = Achievement.objects.all()
    achievements_category = {
        k[1] : AchievementSerializer(achievements.filter(category = k[0]), many=True).data for k in CATEGORY_CHOICES
    }
    years = list(range(2000,datetime.now().year))
    achievements_year = {
        year : AchievementSerializer(achievements.filter(achievedDate__year = year), many=True).data for year in years
    }
    projects = Project.objects.all()
    projects_year = {
        year : ProjectSerializer(projects.filter(endDate__year = year), many=True).data for year in years
    }

    return JsonResponse({
        'achievements_category' : achievements_category,
        'achievements_year' : achievements_year,
        'projects_year' : projects_year
    })
