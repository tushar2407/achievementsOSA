from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.dispatch import receiver

from main.models import Skill

import os
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    dob = models.DateField(null = True, blank = True)
    age = models.PositiveSmallIntegerField(default = 18)

    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'staff'),
        (3, 'admin'),
    )

    designation = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    
    GENDER_CHOICES = (
        (1, 'female'),
        (2, 'male'),
        (3, 'prefer-not-to-say'),
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default = 3)

    profile_pic = models.FileField(null = True, blank = True)
    address = models.TextField(blank = True, null = True)
    group = models.CharField(max_length = 256, blank = True, null = True)
    skills = models.ManyToManyField(Skill, related_name='people', blank = True)
    
    show_email = models.BooleanField(default = False)
    show_phone = models.BooleanField(default = False)
    
    # social media handles
    facebook = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)
    twitter = models.URLField(null = True, blank = True)
    github = models.URLField(null = True, blank = True)

    phone_regex = RegexValidator(regex=r'^\d{8,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True, null=True, blank = True)

    def __str__(self):
        return f'{self.user.username} {str(self.designation)} {self.id}'

    def is_admin(self):
        return self.designation==3

@receiver(models.signals.post_delete, sender=Profile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)