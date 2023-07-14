from django.contrib import admin
from .models import UserProfile, Trip, Message
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Trip)
admin.site.register(Message)