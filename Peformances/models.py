from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.title}' Difficulty {self.description}"


    
class UserPeformance(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time_field = models.TimeField(default='00:00:00', help_text="Enter time in HH:MM:SS format")
    complete = models.DateField()
    content = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.owner.username}'s performance in {self.event.title} "

    class Meta:
        ordering = ['-event']