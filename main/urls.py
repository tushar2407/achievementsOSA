from django.urls import path, include
from main.views import TagViewSet, ProjectViewset, AchievementViewset
from rest_framework import routers

router = routers.DefaultRouter
router.register(r'tag', TagViewSet)
router.register(r'project', ProjectViewset)
router.register(r'achievement', AchievementViewset)

urlpatterns = [
    path('api/', include('router.urls')),    
]