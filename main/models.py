from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Achievement(models.Model):
    title = models.CharField(max_length = 256)
    description = models.TextField()
    technical = models.BooleanField(default = False)
    proof = models.URLField(null = True)
    institution = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add = True)
    achievedDate = models.DateField()
    approved = models.BooleanField(default = False)
    approvedBy = models.ForeignKey(User, on_delete = models.SET_NULL)
    addedBy = models.ForeignKey(User, on_delete = models.SET_NULL)
    teamMembers = models.ManyToManyField(User, related_name='achievements', null = False)
    tags = models.ManyToManyField(Tag, related_name='achievements', null = True)
    
    def __str__(self):
        return f'{self.title}'

class Tag(models.Model):
    title = models.CharField(max_length = 256, unique = True, null = False)    

    def __str__(self):
        return f'{self.title}'