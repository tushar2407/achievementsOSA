from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}' 
   
class Skill(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Education(models.Model):
    institution = models.TextField()
    degree = models.CharField(max_length = 256)
    type = models.CharField(max_length = 256)
    field = models.CharField(max_length = 256)

    def __str__(self):
        return f'{self.institution} {self.degree}'

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeId = models.CharField(max_length = 256, unique = True, null = False)
    associatedSince = models.DateField()
    department = models.ForeignKey(Department, null = False, on_delete = models.CASCADE)
    designation = models.CharField(max_length = 256)

    TITLE_CHOICES = (
        (1, 'Dr.'),
        (2, 'Mr.'),
        (3, 'Mrs.'),
        (4, 'Ms.'),
    )
    title = models.PositiveSmallIntegerField(choices = TITLE_CHOICES)

    education = models.ManyToManyField(Education, related_name = 'staff')

    def __str__(self):
        return f'{self.user.username} {self.employeeId} {self.designation}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollNo = models.CharField(max_length = 256)
    batch = models.PositiveSmallIntegerField()
    # skills = models.ManyToManyField(Skill)
    major = models.CharField(max_length = 256)
    GPA = models.FloatField(default=0.0)
    bio = models.TextField(blank = True)
    website = models.URLField(blank = True)
    education = models.ManyToManyField(Education, related_name = 'students')
    
    def __str__(self):
        return f'{self.user.username} {self.rollNo}'

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length = 256)
    year = models.IntegerField(default = 2021)
    vacancy = models.PositiveSmallIntegerField()
    recruited = models.PositiveSmallIntegerField()
    eligibilityGPA = models.FloatField()

    OFFER_CHOICES = (
        (1, 'Internship'),
        (2, 'Placement'),
    )
    offer = models.PositiveSmallIntegerField(choices = OFFER_CHOICES )

    criteria = models.ManyToManyField(Skill, related_name='companyCriteria')

    def __str__(self):
        return f'{self.user.username} {self.company} {self.year}'