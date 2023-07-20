from django.shortcuts import render, redirect
from profiles.models import Message
# Create your views here.

def feed(request):
    if not request.user.is_authenticated:
        return redirect("../login")
    context = {
        'list_messages': Message.objects.filter(user=request.user).order_by("-id")
    }
    return render(request, 'feed/feed.html', context)
