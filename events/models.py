from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=40)
    attendees = models.ManyToManyField(User, related_name="attendees", null=True)
    description = models.TextField(max_length=200)
    
