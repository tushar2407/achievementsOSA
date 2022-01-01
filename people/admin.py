from django.contrib import admin
from people.models import (
    Skill,
    Education,
    Staff,
    Student,
    Recruiter
)
# Register your models here.

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Recruiter)