from django.shortcuts import render, redirect
from profiles.models import Message, UserProfile
from django.contrib.auth.decorators import login_required
from restcountries import RestCountryApiV2 as rapi
from profiles.forms import FormNewMessage
# Create your views here.

@login_required(redirect_field_name=None)
def feed(request): 
    if request.method == 'POST':
        form_new_message = FormNewMessage(request.POST)
        Message.objects.create(
            user = request.user,
            location = form_new_message.data["location"], 
            message = form_new_message.data["message"]
        )
        return redirect("../feed")
    else:
        form_new_message = FormNewMessage()
    followings = request.user.following["followings"]
    followings.append(request.user)
    context = {
        'list_suggestions': UserProfile.objects.all()[0:5],
        'list_messages': Message.objects.filter(user__in=followings).order_by("-id"),
        'form_new_message': form_new_message,
        'countries': rapi.get_all()
    }
    return render(request, 'feed/feed.html', context)
