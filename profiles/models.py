from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    description = models.TextField(max_length=300, blank=False, null=False, default="No has seleccionado ninguna descripcion")
    nacionality = models.CharField(max_length=100, blank=True)
    image_profile = models.TextField(max_length=None, blank=True)
    image_portate = models.TextField(max_length=None, blank=True)
    #my_trips = models.JSONField(blank=True, null=True)
    #my_future_trips = models.JSONField(blank=True, null=True)

class Trip(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    images = models.JSONField(blank=False, null=False)

    def __str__(self):
        return f'{self.user} {self.title}'