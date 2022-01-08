from django.contrib.auth.views import LogoutView
from django.urls import path, include
from authenticate.views import (
    CustomLoginView, 
    ProfileViewset, 
    approve_users,
)
from rest_framework import routers 


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', CustomLoginView.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('api/approve-users', approve_users, name="approve_users")
]