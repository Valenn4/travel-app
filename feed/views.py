from django.shortcuts import render, redirect
from profiles.models import Message
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name=None)
def feed(request):
    context = {
        'list_messages': Message.objects.filter(user=request.user).order_by("-id")
    }
    return render(request, 'feed/feed.html', context)
