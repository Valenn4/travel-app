from django.shortcuts import render, redirect
from profiles.models import Message, UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name=None)
def feed(request): 
    followings = request.user.following["followings"]
    followings.append(request.user)
    context = {
        'list_suggestions': UserProfile.objects.all()[::5],
        'list_messages': Message.objects.filter(user__in=followings).order_by("-id"),
    }
    return render(request, 'feed/feed.html', context)
