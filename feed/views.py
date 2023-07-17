from django.shortcuts import render, redirect
from .forms import FormNewMessage
from profiles.models import Message
# Create your views here.

def feed(request):
    if request.method == 'POST':
        form_new_message = FormNewMessage(request.POST)
        Message.objects.create(
            user = request.user,
            message = form_new_message.data["message"]
        )
        return redirect("../feed")
    else:
        form_new_message = FormNewMessage()
    context = {
        'form_new_message': form_new_message,
        'list_messages': Message.objects.filter(user=request.user).order_by("-id")
    }
    return render(request, 'feed/feed.html', context)
