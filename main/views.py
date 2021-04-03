from django.shortcuts import render
from main.serializers import TagSerializer, ProjectSerializer, AchievementSerializer
from main.models import Tag, Project, Achievement
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
class AchievementViewset(viewsets.ModelViewSet):
    serialzier_class = AchievementSerializer
    queryset = Achievement.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
