from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from achievements.settings import USER_CREDS_URL
from authenticate.models import Profile, Phone
from authenticate.serializers import ProfileSerializer, PhoneSerializer
from main.utils import get_achievements_json_format, get_projects_json_format

import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
# Create your views here.

@csrf_exempt
def login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        request = Request(USER_CREDS_URL, urlencode({
            'username': username,
            'password' : password
        }).encode())
        response = json.loads(urlopen(request).read().decode())

        if response.get('token'):
            # User exists in main DB
            user = User.objects.get_or_create(
                username = response['user']['username_osa']
            )[0]
            # print(user)
            profile = ProfileSerializer(
                    Profile.objects.get_or_create(
                        user = user
                    )[0]
                ).data
            profile['username'] = user.username
            profile['name'] = user.first_name + " " + user.last_name
            profile['is_admin'] = (profile['designation']==3)

            return JsonResponse({
                "profile" : profile,
                "token" : Token.objects.get_or_create(user = user)[0].key
            })

        else:
            return JsonResponse(response)

    return JsonResponse({
        "error": f"{request.method} is not allowed on this endpoint."
    })

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        r  = Response(data = self.serializer_class(Profile.objects.get(user=user)).data)
        r.data['name'] = user.first_name+ " " + user.last_name
        r.data['username'] = user.username
        r.data['achievements'] = get_achievements_json_format(user)
        r.data['projects'] = get_projects_json_format(user)
        return r

    def list(self, request, *args, **kwargs):
        profile = self.serializer_class(Profile.objects.get(user=request.user)).data
        profile['name'] = request.user.first_name+ " " + request.user.last_name
        profile['username'] = request.user.username
        profile['achievements'] = get_achievements_json_format(self.request.user)
        profile['projects'] = get_projects_json_format(self.request.user)

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