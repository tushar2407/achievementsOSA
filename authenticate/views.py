from django.shortcuts import render
from authenticate.serializers import ProfileSerializer, PhoneSerializer
from authenticate.models import Profile, Phone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self, request):
        return Profile.objects.get(username = request.username)
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk= Profile.objects.get(username = request.username).id
        return super().partial_update(request, pk, *args, **kwargs)

class PhoneViewset(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self, request):
        return Phone.objects.filter(user = request.user)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)