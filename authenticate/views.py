from django.shortcuts import render
from authenticate.serializers import ProfileSerializer, PhoneSerializer
from authenticate.models import Profile, Phone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http.response import JsonResponse
# Create your views here.

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        profile = ProfileSerializer(Profile.objects.get(user=request.user)).data
        profile['name'] = request.user.first_name+ " " + request.user.last_name
        profile['username'] = request.user.username
        return JsonResponse(
            {'profile' : profile}
        )
    
    def partial_update(self, request, pk, *args, **kwargs):
        pk= Profile.objects.get(user = request.user).id
        return super().partial_update(request, pk, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class PhoneViewset(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self, *args, **kwargs):
        return Phone.objects.filter(user = self.request.user)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)