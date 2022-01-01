from django.urls import path, include
from rest_framework import routers
from people.views import (
    EducationViewset,
    SkillViewset,
    StaffViewset,
    StudentViewset,
    RecruiterViewset
)

router = routers.DefaultRouter()
router.register(r'education', EducationViewset)
router.register(r'skill', SkillViewset)
router.register(r'staff', StaffViewset)
router.register(r'student', StudentViewset)
router.register(r'recruiter', RecruiterViewset)

urlpatterns = [
    path('api/', include(router.urls))
]