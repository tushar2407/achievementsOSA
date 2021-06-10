from django.urls import path, include
from authenticate.views import (
    ProfileViewset, 
    PhoneViewset,
    login
)
from rest_framework import routers 


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewset)
router.register(r'phone', PhoneViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', login, name = "login")
]