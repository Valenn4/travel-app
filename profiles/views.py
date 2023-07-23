import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormNewTravel, FormChangeUser, FormAddImage, FormNewMessage
from .models import Trip, UserProfile, Message
from firebase_admin import storage
from django.contrib.auth.decorators import login_required

from restcountries import RestCountryApiV2 as rapi
# Create your views here.

def get_image_user(request, image, user):
    bucket = storage.bucket()
    blob = bucket.blob(f"users/{user}/{image}")
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

def get_image_trip(request, location, image, user):
    bucket = storage.bucket()
    blob = bucket.blob(f"trips/{user}/{location}/{image}")
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

def get_image_portate(request, image, user):
    bucket = storage.bucket()
    blob = bucket.blob(f"portate/{user}/{image}")
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

@login_required(redirect_field_name=None)
def profile(request, user):
    user = UserProfile.objects.get(username=user)
    # TRIPS
    trips = []
    for trip in Trip.objects.filter(user=user).order_by("-id"):
        list_images = json.loads(trip.images.get("images"))
        trips.append({"id": trip.id, "title": trip.title, "location":trip.location, "images":list_images, "last_image":list_images[len(list_images)-1]})
    # MESSAGGES
    messages = Message.objects.filter(user=user).order_by("-id")
    
    context = {
        'user_connected': user,
        'trips':trips,
        'list_messages': Message.objects.filter(user=user).order_by("-id")
    }
    return render(request, 'profile/profile.html', context)

@login_required(redirect_field_name=None)
def edit_profile(request):
    if request.method == "POST":
        print(request.POST)
        form = FormChangeUser(request.POST, request.FILES, instance=request.user)
        
        bucket = storage.bucket()
        
        user = UserProfile.objects.get(id=request.user.id)
        user.description = form.data["description"]
        user.nacionality = form.data["nacionality"]
        if(request.FILES.get("image_profile") != None):
            image_last = bucket.blob(f'users/{request.user}/{request.user.image_profile}')
            image_last.delete()
            user.image_profile = request.FILES.get("image_profile").name
            blob = bucket.blob(f'users/{request.user}/'+request.FILES.get("image_profile").name)
            blob.upload_from_file(request.FILES.get("image_profile"))
        if(request.FILES.get("image_portate") != None):
            image_last = bucket.blob(f'portate/{request.user}/{request.user.image_portate}')
            image_last.delete()
            user.image_portate = request.FILES.get("image_portate").name
            blob = bucket.blob(f'portate/{request.user}/'+request.FILES.get("image_portate").name)
            blob.upload_from_file(request.FILES.get("image_portate"))
        user.save()
    
        return redirect("../../profile")
    else:
        form = FormChangeUser(instance = request.user)
    context = {
        'user': UserProfile.objects.get(id=request.user.id),
        'form': form,
        'countries': rapi.get_all()
    }
    return render(request, 'profile/edit_profile.html', context)

@login_required(redirect_field_name=None)
def new_trip(request):
    if request.method=='POST':
        form = FormNewTravel(request.POST, request.FILES)
        
        if(Trip.objects.filter(user = request.user,title=form.data["title"]).exists()):
            result = "Ya existe un viaje con el mismo nombre"
        else:
            list_images = []
            for image in request.FILES.getlist("image"):
                bucket = storage.bucket()
                blob = bucket.blob(f'trips/{request.user}/'+form.data["location"]+"/"+image.name)
                blob.upload_from_file(image)
                list_images.append(image.name)
                
            Trip.objects.create(
                user = request.user,
                location = form.data["location"],
                title = form.data["title"],
                images = {"images":json.dumps(list_images)}
            )
            result = "Viaje creado exitosamente"
            return redirect("../profile")
    else:
        form = FormNewTravel()
        result = ""
    context={
        "form":form,
        "result":result,
        'countries': rapi.get_all()
    }
    return render(request, 'profile/new_trip.html', context)

@login_required(redirect_field_name=None)
def new_message(request):
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
    context = {
        'form_new_message': form_new_message,
        'countries': rapi.get_all()
    }
    return render(request, 'profile/new_message.html', context)

@login_required(redirect_field_name=None)
def trip (request, id):
    trip = Trip.objects.get(id=id)
    list_images =json.loads(trip.images.get("images"))
    list_images.reverse()
    if request.method == 'POST' and request.FILES:
        form = FormAddImage(request.POST)
        image = request.FILES['image']
        if(image.name in list_images):
            result_form = "Ya existe la imagen en el album"
        else:
            images = json.loads(trip.images.get("images"))
            images.append(image.name)
            
            trip.images = {"images":json.dumps(images)}
            trip.save()
            bucket = storage.bucket()
            blob = bucket.blob(f'trips/{Trip.objects.get(id=id).user.username}/'+trip.location+"/"+image.name)
            blob.upload_from_file(image) 
            
            result_form = ""   
            return redirect(f"../../trip/{id}")

    else:
        form = FormAddImage(request.POST)
        result_form = ""     
   
    context = {
        'trip':trip,
        'images':list_images,
        'result_form': result_form,
        'form': form,
        'user_trip': Trip.objects.get(id=id).user.username
    }
    return render(request, 'profile/trip.html', context)
