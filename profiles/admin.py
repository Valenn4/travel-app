from django.contrib import admin
from .models import UserProfile, Trip, Publication
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Trip)
admin.site.register(Publication)