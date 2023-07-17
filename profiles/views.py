import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormNewTravel, FormChangeUser, FormAddImage
from .models import Trip, UserProfile, Message
from firebase_admin import storage
from django.contrib import auth
# Create your views here.

def get_image_user(request, image):
    bucket = storage.bucket()
    blob = bucket.blob(f"users/{request.user.username}/{image}")
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

def get_image_trip(request, location, image):
    bucket = storage.bucket()
    blob = bucket.blob(f"trips/{request.user.username}/{location}/{image}")
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

def get_image_portate(request, image):
    bucket = storage.bucket()
    blob = bucket.blob(f"portate/{request.user.username}/{image}")
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))


def profile(request):
    if request.user.is_authenticated == False:
        return redirect("../login")
    # TRIPS
    trips = []
    for trip in Trip.objects.filter(user=request.user).order_by("-id"):
        list_images = json.loads(trip.images.get("images"))
        trips.append({"id": trip.id, "title": trip.title, "location":trip.location, "images":list_images, "last_image":list_images[len(list_images)-1]})
    # MESSAGGES
    messages = Message.objects.filter(user=request.user).order_by("-id")
    '''
    if request.method == 'POST':
        form_new_message = FormNewMessage(request.POST)
        if form_new_message.is_valid():
            new_message = Message.objects.create(
                user = request.user,
                message = form_new_message.data["message"],
            )
            new_message.save()
        context = {
            'trips':trips,
            'messages': messages,
            'form_new_message': FormNewMessage(),
            'message_condition': True
        }
        return render(request, 'profile/profile.html', context)
    else:
        form_new_message = FormNewMessage()
    '''
    context = {
        'trips':trips,
        'messages': messages,
    }
    return render(request, 'profile/profile.html', context)

def edit_profile(request, id):
    if request.user.is_authenticated == False:
        return redirect("../login")
    if request.method == "POST":
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
        'user': UserProfile.objects.get(id=id),
        'form': form
    }
    return render(request, 'profile/edit_profile.html', context)

def new_trip(request):
    if request.user.is_authenticated == False:
        return redirect("../login")
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
        "result":result
    }
    return render(request, 'profile/new_trip.html', context)

def trip (request, id): 
    if request.user.is_authenticated == False:
        return redirect("../login")
    
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
            blob = bucket.blob(f'trips/{request.user}/'+trip.location+"/"+image.name)
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
        'form': form
    }
    return render(request, 'profile/trip.html', context)
