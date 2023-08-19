from django.db import models
from profiles.models import UserProfile
from restcountries import RestCountryApiV2 as rapi
# Create your models here.

list_countries = []
for el in rapi.get_all():
    list_countries.append((el.name, el.name))

class Message(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField(max_length=None, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
class LivingRoom(models.Model):
    created_by = models.ForeignKey(UserProfile, related_name="livingrooms", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    nacionality = models.CharField(max_length=100, choices=tuple(list_countries), blank=False)
    members = models.ManyToManyField(UserProfile, blank=True, null=True)
    messages = models.ManyToManyField(Message, blank=True, null=True)
    def __str__(self):
        return self.name


