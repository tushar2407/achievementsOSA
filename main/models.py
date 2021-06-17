from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from people.models import Student, Staff

class Institution(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Tag(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Achievement(models.Model):
    title = models.CharField(max_length = 256)
    description = models.TextField()
    technical = models.BooleanField(default = False)
    proof = models.URLField(null = True)
    institution = models.ForeignKey(Institution, null = True, blank = True, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add = True)
    achievedDate = models.DateField()
    approved = models.BooleanField(default = False)
    approvedBy = models.ForeignKey(Staff, on_delete = models.DO_NOTHING, null = True)
    addedBy = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    mentors = models.ManyToManyField(Staff, related_name='achievements', blank = True)
    teamMembers = models.ManyToManyField(User, related_name='achievements', blank = True)
    tags = models.ManyToManyField(Tag, related_name='achievements', blank = True)
    CATEGORY_CHOICES = (
        (0, 'NA'),
        (1,'intra college'), 
        (2,'inter college'), 
        (3,'district level'),
        (4,'state level'), 
        (5,'national level'), 
        (6,'international level')
    )
    category = models.PositiveSmallIntegerField(choices = CATEGORY_CHOICES, default = 1)
    
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    addedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null = True)
    approved = models.BooleanField(default = False)
    approvedBy = models.ForeignKey(Staff, on_delete = models.DO_NOTHING, null = True)
    title = models.CharField(max_length = 256)
    description = models.TextField()
    mentors = models.ManyToManyField(Staff, related_name='projects', blank = True)
    students = models.ManyToManyField(Student, related_name='projects', blank = True)
    startDate = models.DateField()
    endDate = models.DateField()
    field = models.CharField(max_length = 256, null = False)
    domain = models.CharField(max_length = 256, null = False)
    tags = models.ManyToManyField(Tag, related_name='projects', blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'