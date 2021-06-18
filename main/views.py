from django.contrib.auth.models import User
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from authenticate.models import Profile
from main.models import Tag, Project, Achievement, Institution
from main.serializers import (
    TagSerializer, 
    ProjectSerializer, 
    AchievementSerializer, 
    InstitutionSerializer,
    UserSerializer
)
from people.models import Staff, Student
from people.serializers import StaffSerializer, StudentSerializer
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

    def list(self, *args, **kwargs):
        projects = list(map(lambda x : dict(x), self.serializer_class(Project.objects.filter(addedBy = self.request.user)\
            .prefetch_related('tags', 'mentors', 'students')\
            .select_related('addedBy', 'approvedBy'), many = True).data))

        for i in projects:

            u = User.objects.get(id = i['addedBy'])
            i['addedBy'] =  dict(UserSerializer(u).data)
        
            if i['approvedBy']:
                i['approvedBy'] = StaffSerializer(Staff.objects.get(id = i['approvedBy'])).data        
            
            if i['tags']:
                i['tags'] = list(map(lambda x : dict(x), TagSerializer(Tag.objects.filter(id__in = i['tags']), many=True).data))
        
            if i['mentors']:
                i['mentors'] = list(map(lambda x : dict(x), StaffSerializer(Staff.objects.filter(id__in = i['mentors']), many=True).data))
        
            if i['students']:
                i['students'] = list(map(lambda x : dict(x), StudentSerializer(Student.objects.filter(id__in = i['teamMembers']), many=True).data))
        
        return JsonResponse({'projects' : projects})
    
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

    def list(self, *args, **kwargs):
        achievements = list(map(lambda x : dict(x), self.serializer_class(Achievement.objects.filter(addedBy = self.request.user)\
            .prefetch_related('tags', 'mentors', 'teamMembers')\
            .select_related('addedBy', 'approvedBy'), many = True).data))

        for i in achievements:

            u = User.objects.get(id = i['addedBy'])
            i['addedBy'] =  dict(UserSerializer(u).data)
        
            if i['approvedBy']:
                i['approvedBy'] = StaffSerializer(Staff.objects.get(id = i['approvedBy'])).data        
            
            if i['tags']:
                i['tags'] = list(map(lambda x : dict(x), TagSerializer(Tag.objects.filter(id__in = i['tags']), many=True).data))
        
            if i['mentors']:
                i['mentors'] = list(map(lambda x : dict(x), StaffSerializer(Staff.objects.filter(id__in = i['mentors']), many=True).data))
        
            if i['teamMembers']:
                i['teamMembers'] = list(map(lambda x : dict(x), UserSerializer(User.objects.filter(id__in = i['teamMembers']), many=True).data))
        
        return JsonResponse({'achievements' : achievements})

    # def partial_update(self, request, pk, *args, **kwargs):
    #     pk= request.user.id
    #     return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(addedBy = self.request.user)

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
        # approved = list(Achievement.objects.filter(approved = True))
        unapproved = list(Achievement.objects.filter(approved = False).values.values())
        
        return JsonResponse(
            {
                # 'approved': approved,
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
        # approved = list(Achievement.objects.filter(approved = True))
        unapproved = list(Project.objects.filter(approved = False).values())
        
        return JsonResponse(
            {
                # 'approved': approved,
                'unapproved': unapproved
            }
        )
    return JsonResponse(
        {
            'details': 'Not an admin'
        }
    )
