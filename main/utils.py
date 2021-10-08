from django.contrib.auth.models import User
from main.models import Tag, Project, Achievement, Institution
from main.serializers import (
    TagSerializer, 
    ProjectSerializer, 
    AchievementSerializer, 
    InstitutionSerializer,
    UserSerializer
)
from people.models import Staff, Student
from people.serializers import StaffSerializer, StudentSerializer

def get_achievements_json_format(user):
    achievements = AchievementSerializer(Achievement.objects.filter(addedBy = user)\
            .prefetch_related('tags', 'mentors', 'teamMembers')\
            .select_related('addedBy', 'approvedBy', 'institution'), many = True).data

    for i in achievements:

        u = User.objects.get(id = i['addedBy'])
        i['addedBy'] =  UserSerializer(u).data
    
        if i['approvedBy']:
            i['approvedBy'] = StaffSerializer(Staff.objects.get(id = i['approvedBy'])).data        
        
        if i['institution']:
            i['institution'] = InstitutionSerializer(Institution.objects.get(id = i['institution'])).data        
        
        if i['tags']:
            i['tags'] = TagSerializer(Tag.objects.filter(id__in = i['tags']), many=True).data
    
        if i['mentors']:
            i['mentors'] = StaffSerializer(Staff.objects.filter(id__in = i['mentors']), many=True).data
    
        if i['teamMembers']:
            i['teamMembers'] = UserSerializer(User.objects.filter(id__in = i['teamMembers']), many=True).data
        
        return achievements

def get_projects_json_format(user):
    projects = ProjectSerializer(Project.objects.filter(addedBy = user)\
            .prefetch_related('tags', 'mentors', 'students')\
            .select_related('addedBy', 'approvedBy', 'institution'), many = True).data

    for i in projects:

        u = User.objects.get(id = i['addedBy'])
        i['addedBy'] =  UserSerializer(u).data
    
        if i['approvedBy']:
            i['approvedBy'] = StaffSerializer(Staff.objects.get(id = i['approvedBy'])).data        
        
        if i['institution']:
            i['institution'] = InstitutionSerializer(Institution.objects.get(id = i['institution'])).data        
        
        if i['tags']:
            i['tags'] = TagSerializer(Tag.objects.filter(id__in = i['tags']), many=True).data
    
        if i['mentors']:
            i['mentors'] = StaffSerializer(Staff.objects.filter(id__in = i['mentors']), many=True).data
    
        if i['students']:
            i['students'] = StudentSerializer(Student.objects.filter(id__in = i['teamMembers']), many=True).data
    
    return projects
        