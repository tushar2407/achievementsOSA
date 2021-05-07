from django.urls import path, include
from main.views import (
    TagViewSet, 
    ProjectViewset, 
    AchievementViewset, 
    homepage,
    get_professors,
    get_students
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet)
router.register(r'project', ProjectViewset)
router.register(r'achievement', AchievementViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('homepage/', homepage, name = "homepage"),
    path('api/get-professors', get_professors),  
    path('api/get-students', get_students)    
]