from django.shortcuts import render, redirect
from profiles.models import Message, UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name=None)
def feed(request):
    if request.method == 'POST':
        result = request.POST['result']
        context = {
            'list_messages': Message.objects.filter(user=request.user).order_by("-id"),
            'flag_search': True,
            'list_users': UserProfile.objects.filter(username__contains=result)
        }
        return render(request, 'feed/feed.html', context)    
    context = {
        'list_messages': Message.objects.filter(user=request.user).order_by("-id"),
        'flag_search': False,
    }
    return render(request, 'feed/feed.html', context)
