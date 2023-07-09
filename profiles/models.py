from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    description = models.TextField(max_length=300, blank=True)
    nacionality = models.CharField(max_length=100, blank=False)
    my_trips = models.JSONField(blank=True, null=True)
    my_future_trips = models.JSONField(blank=True, null=True)

class Image(models.Model):
    image = models.ImageField(upload_to="images/")