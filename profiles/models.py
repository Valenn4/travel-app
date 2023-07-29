from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.forms import ValidationError
from restcountries import RestCountryApiV2 as rapi
# Create your models here.

list_countries = []
for el in rapi.get_all():
    list_countries.append((el.name, el.name))

class UserProfile(AbstractUser):
    description = models.TextField(max_length=300, blank=False, null=False, default="No has seleccionado ninguna descripcion")
    nacionality = models.CharField(max_length=100, blank=True)
    image_profile = models.TextField(max_length=None, blank=True)
    image_portate = models.TextField(max_length=None, blank=True)
    following = models.JSONField(blank=True, default={'followings':[]})

class Trip(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=200, choices=tuple(list_countries), blank=False)
    images = models.JSONField(blank=False, null=False)

    def __str__(self):
        return f'{self.user} {self.title}'



class Message(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, choices=tuple(list_countries), blank=False)
    message = models.TextField(max_length=150, blank=False, null=False)
    date = models.DateTimeField(auto_now=True, null=False, blank=False)
    likes = models.IntegerField(default=0, blank=False, null=False)