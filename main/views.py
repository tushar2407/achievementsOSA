from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render
from main.serializers import TagSerializer, ProjectSerializer, AchievementSerializer, InstitutionSerializer
from main.models import Tag, Project, Achievement, Institution
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from people.models import Staff, Student
from authenticate.models import Profile
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

    def get_queryset(self):
        return Project.objects.filter(addedBy = self.request.user)
    
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

    def get_queryset(self):
        return Achievement.objects.filter(addedBy = self.request.user)
    
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
