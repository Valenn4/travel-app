from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Message, LivingRoom
from profiles.models import UserProfile
# Create your views here.


def chat(request, uuid):
    context = {
        "messages":LivingRoom.objects.get(name=uuid)
    }
    return render(request, 'chat/chat.html', context)


@require_POST
def new_message(request, room):
    message = Message.objects.create(
        message = request.POST["message"],
        created_by = UserProfile.objects.get(username = request.POST["created_by"])
    )
    room = LivingRoom.objects.get(name=room)
    room.messages.add(message)
    room.save()
    return JsonResponse({"message":"Mensaje enviado"})