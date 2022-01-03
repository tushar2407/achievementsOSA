from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = (
    (0, 'NA'),
    (1,'intra college'), 
    (2,'inter college'), 
    (3,'district level'),
    (4,'state level'), 
    (5,'national level'), 
    (6,'international level')
)

class Institution(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Education(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True)
    degree = models.CharField(max_length = 256)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.institution} {self.degree} {self.id}'

class Tag(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Skill(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeId = models.CharField(max_length = 256, unique = True, null = False)
    associatedSince = models.DateField()
    department = models.CharField(max_length = 256, blank=True)
    designation = models.CharField(max_length = 256)

    TITLE_CHOICES = (
        (1, 'Dr.'),
        (2, 'Mr.'),
        (3, 'Mrs.'),
        (4, 'Ms.'),
    )
    title = models.PositiveSmallIntegerField(choices = TITLE_CHOICES)

    education = models.ManyToManyField(Education, related_name = 'staffs')

    def __str__(self):
        return f'{self.user.username} {self.employeeId} {self.designation} {self.id}'

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
        return f'{self.user.username} {self.rollNo} {self.id}'

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

class Achievement(models.Model):
    addedBy = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    approved = models.CharField(max_length = 10, default = "Pending")
    approvedBy = models.ForeignKey(Staff, on_delete = models.DO_NOTHING, null = True, blank = True)
    achievedDate = models.DateField()
    dateCreated = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    institution = models.ForeignKey(Institution, null = True, blank = True, on_delete=models.CASCADE)
    mentors = models.ManyToManyField(Staff, related_name='achievements', blank = True)
    proof = models.URLField(null = True, max_length=1000)
    tags = models.ManyToManyField(Tag, related_name='achievements', blank = True)
    teamMembers = models.ManyToManyField(User, related_name='achievements', blank = True)
    technical = models.BooleanField(default = False)
    title = models.CharField(max_length = 256)
    
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