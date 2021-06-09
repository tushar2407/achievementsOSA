from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
from people.models import Skill

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    dob = models.DateField()
    age = models.PositiveSmallIntegerField()

    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'staff'),
        (3, 'admin'),
    )

    designation = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    
    GENDER_CHOICES = (
        (1, 'female'),
        (2, 'male'),
        (3, 'prefer-not-to-say'),
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)

    profile_pic = models.TextField(null = True)
    address = models.TextField()
    group = models.CharField(max_length = 256)
    skills = models.ManyToManyField(Skill, related_name='people')
    
    show_email = models.BooleanField(default = False)
    show_phone = models.BooleanField(default = False)
    
    # social media handles
    facebook = models.URLField(null = True)
    instagram = models.URLField(null = True)
    twitter = models.URLField(null = True)
    github = models.URLField(null = True)

    def __str__(self):
        return f'{self.user.username} {str(self.designation)}'

    def is_admin(self):
        return self.designation==3

class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\d{8,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    number = models.CharField(verbose_name = 'phone_number',validators=[phone_regex], max_length=13, unique=True, null=False, blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = False, related_name='phone_numbers')

    def __str__(self):
        return f'{self.number} {self.user.username}'