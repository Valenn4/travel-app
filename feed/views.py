from django.shortcuts import render, redirect
from profiles.models import Message, UserProfile, Trip
from django.contrib.auth.decorators import login_required
from restcountries import RestCountryApiV2 as rapi
from profiles.forms import FormNewMessage, FormNewTravel
import json
from firebase_admin import storage

# Create your views here.

@login_required(redirect_field_name=None)
def feed(request): 
    if request.method == 'POST':
        if 'form_new_message' in request.POST:
            form_new_message = FormNewMessage(request.POST)
            if form_new_message.is_valid():
                Message.objects.create(
                    user = request.user,
                    location = form_new_message.data["location"], 
                    message = form_new_message.data["message"]
                )
                return redirect("../feed")
            else:
                form_new_message = FormNewMessage()
        if 'form_new_trip' in request.POST:
            form_new_trip = FormNewTravel(request.POST, request.FILES)
            if(Trip.objects.filter(user = request.user,title=form_new_trip.data["title"]).exists()==False):
                list_images = []
                for image in request.FILES.getlist("image"):
                    bucket = storage.bucket()
                    blob = bucket.blob(f'trips/{request.user}/'+form_new_trip.data["location"]+"/"+image.name)
                    blob.upload_from_file(image)
                    list_images.append(image.name)
                    
                Trip.objects.create(
                    user = request.user,
                    location = form_new_trip.data["location"],
                    title = form_new_trip.data["title"],
                    images = {"images":json.dumps(list_images)}
                )
                return redirect(f'../profile/{request.user.username}')
            else:
                form_new_trip = FormNewTravel()
        form_new_message = FormNewMessage()
        form_new_trip = FormNewTravel()
    else:
        form_new_message = FormNewMessage()
        form_new_trip = FormNewTravel()
    followings = request.user.following["followings"]
    followings.append(request.user)
    context = {
        'list_suggestions': UserProfile.objects.all()[0:5],
        'list_messages': Message.objects.filter(user__in=followings).order_by("-id"),
        'form_new_message': form_new_message,
        'form_new_trip': form_new_trip,
    }
    return render(request, 'feed/feed.html', context)

@login_required(redirect_field_name=None)
def countries_search(request, country):
    if request.method == 'POST':
        if 'form_new_message' in request.POST:
            form_new_message = FormNewMessage(request.POST)
            if form_new_message.is_valid():
                Message.objects.create(
                    user = request.user,
                    location = form_new_message.data["location"], 
                    message = form_new_message.data["message"]
                )
                return redirect("../feed")
            else:
                form_new_message = FormNewMessage()
        if 'form_new_trip' in request.POST:
            form_new_trip = FormNewTravel(request.POST, request.FILES)
            if(Trip.objects.filter(user = request.user,title=form_new_trip.data["title"]).exists()==False):
                list_images = []
                for image in request.FILES.getlist("image"):
                    bucket = storage.bucket()
                    blob = bucket.blob(f'trips/{request.user}/'+form_new_trip.data["location"]+"/"+image.name)
                    blob.upload_from_file(image)
                    list_images.append(image.name)
                    
                Trip.objects.create(
                    user = request.user,
                    location = form_new_trip.data["location"],
                    title = form_new_trip.data["title"],
                    images = {"images":json.dumps(list_images)}
                )
                return redirect(f'../profile/{request.user.username}')
            else:
                form_new_trip = FormNewTravel()
        form_new_message = FormNewMessage()
        form_new_trip = FormNewTravel()
    else:
        form_new_message = FormNewMessage()
        form_new_trip = FormNewTravel()
    context = {
        'list_suggestions': UserProfile.objects.all()[0:5],
        'messages_country': Message.objects.filter(location=country),
        'form_new_message': form_new_message,
        'form_new_trip': form_new_trip,
    }
    return render(request, 'feed/countries_search.html', context)