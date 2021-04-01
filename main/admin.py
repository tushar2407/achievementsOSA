from django.contrib import admin
from main.models import Tag, Achievement, Project
# Register your models here.

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Achievement)