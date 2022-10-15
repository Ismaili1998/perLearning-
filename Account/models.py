from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Skill(models.Model):
        skill_name = models.CharField(max_length=200)
        score = models.models.IntegerField(default=0,
        max_length = 3
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    education_level = models.CharField(null=True, Blank=True)
    user_image = models.ImageField(upload_to='user_images/',null=True)
    skills = models.ManyToManyField(Skill)
    engagement_score = models.models.IntegerField(default=0,
        max_length = 3
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



