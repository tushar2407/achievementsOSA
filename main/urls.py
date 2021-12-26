from django.urls import path, include
from main.views import (
    AchievementViewset, 
    InstitutionViewset,
    ProjectViewset, 
    TagViewSet, 
    get_graph_data,
    get_professors,
    get_students,
    get_achievements_admin,
    get_projects_admin,
    homepage,
    search
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet)
router.register(r'project', ProjectViewset)
router.register(r'achievement', AchievementViewset)
router.register(r'institution', InstitutionViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('homepage/', homepage, name = "homepage"),
    path('api/get-professors', get_professors),  
    path('api/get-students', get_students)    ,
    path('api/get-achievements-admin', get_achievements_admin),
    path('api/get-projects-admin', get_projects_admin),
    path('api/search', search),
    path('api/graph', get_graph_data),
]