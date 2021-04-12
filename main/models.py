from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from people.models import Student, Staff

class Tag(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Achievement(models.Model):
    title = models.CharField(max_length = 256)
    description = models.TextField()
    technical = models.BooleanField(default = False)
    proof = models.URLField(null = True)
    institution = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add = True)
    achievedDate = models.DateField()
    approved = models.BooleanField(default = False)
    approvedBy = models.ForeignKey(Staff, on_delete = models.DO_NOTHING, null = True)
    addedBy = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    teamMembers = models.ManyToManyField(User, related_name='achievements')
    tags = models.ManyToManyField(Tag, related_name='achievements')
    
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    addedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null = True)
    title = models.CharField(max_length = 256)
    description = models.TextField()
    mentors = models.ManyToManyField(Staff)
    students = models.ManyToManyField(Student)
    startDate = models.DateField()
    endDate = models.DateField()
    field = models.CharField(max_length = 256, null = False)
    domain = models.CharField(max_length = 256, null = False)
    tags = models.ManyToManyField(Tag, related_name='projects')
    dateCreated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.title}'