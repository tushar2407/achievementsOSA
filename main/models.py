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
    addedBy = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    approved = models.CharField(max_length = 10, default = "Pending")
    approvedBy = models.ForeignKey(Staff, on_delete = models.DO_NOTHING, null = True, blank = True)
    achievedDate = models.DateField()
    dateCreated = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    institution = models.ForeignKey(Institution, null = True, blank = True, on_delete=models.CASCADE)
    mentors = models.ManyToManyField(Staff, related_name='achievements', blank = True)
    proof = models.URLField(null = True)
    tags = models.ManyToManyField(Tag, related_name='achievements', blank = True)
    teamMembers = models.ManyToManyField(User, related_name='achievements', blank = True)
    technical = models.BooleanField(default = False)
    title = models.CharField(max_length = 256)
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
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    addedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null = True)
    approved = models.CharField(max_length = 10, default = "Pending")
    approvedBy = models.ForeignKey(Staff, on_delete = models.DO_NOTHING, null = True, blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    domain = models.CharField(max_length = 256, null = False)
    endDate = models.DateField()
    field = models.CharField(max_length = 256, null = False)
    institution  = models.ForeignKey(Institution, null = True, blank = False, on_delete=models.CASCADE)
    mentors = models.ManyToManyField(Staff, related_name='projects', blank = True)
    startDate = models.DateField()
    students = models.ManyToManyField(Student, related_name='projects', blank = True)
    title = models.CharField(max_length = 256)
    tags = models.ManyToManyField(Tag, related_name='projects', blank = True)
    url = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'