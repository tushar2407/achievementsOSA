from django.urls import path, include
from rest_framework import routers
from people.views import (
    DepartmentViewset,
    EducationViewset,
    SkillViewset,
    StaffViewset,
    StudentViewset
)

router = routers.DefaultRouter()
router.register(r'department', DepartmentViewset)
router.register(r'education', EducationViewset)
router.register(r'skill', SkillViewset)
router.register(r'staff', StaffViewset)
router.register(r'student', StudentViewset)

urlpatterns = [
    path('api/', include('router.urls'))
]