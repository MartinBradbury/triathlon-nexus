from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (NOT_IDENTIFIED, 'Not Identified'),
    ]

    FITNESS_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
        (UNKNOWN, 'Unknown')
    ]


    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=NOT_IDENTIFIED,
    )
    fitness_level = models.CharField(
        max_length=1,
        choices=FITNESS_CHOICES,
        default=UNKNOWN,
    )
    image = models.ImageField(
        upload_to = 'images/', default='../default_profile_qtk8ec'
    )
    content = models.TextField(blank=True)
    progress = models.IntegerField(blank=True)

