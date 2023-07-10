import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormNewTravel
from .models import Trip, UserProfile
from firebase_admin import storage
# Create your views here.

def get_image_trip(request, location, image):
    bucket = storage.bucket()
    blob = bucket.blob(f"trips/{request.user.username}/{location}/{image}")
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

def get_image_user(request, image):
    bucket = storage.bucket()
    blob = bucket.blob(f"users/{request.user.username}/{image}")
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))

def profile(request):

    trips = []
    for trip in Trip.objects.filter(user=request.user).order_by("-id"):
        list_images = json.loads(trip.images.get("images"))
        trips.append({"id": trip.id, "title": trip.title, "location":trip.location, "images":list_images, "last_image":list_images[len(list_images)-1]})
    context = {
        'trips':trips,
    }
    return render(request, 'profile.html', context)

def new_trip(request):
    if request.method=='POST':
        form = FormNewTravel(request.POST,  request.FILES)
        image = request.FILES.get("image")
        bucket = storage.bucket()
        blob = bucket.blob(f'trips/{request.user}/'+form.data["location"]+"/"+image.name)
        blob.upload_from_file(image)

        if(Trip.objects.filter(user = request.user,title=form.data["title"]).exists()):
            result = "Ya existe un viaje con el mismo nombre"
        else:
            list_images = []
            list_images.append(image.name)
            Trip.objects.create(
                user = request.user,
                location = form.data["location"],
                title = form.data["title"],
                images = {"images":json.dumps(list_images)}
            )
            result = "Viaje creado exitosamente"
    else:
        form = FormNewTravel()
        result = ""

    
    context={
        "form":form,
        "result":result
    }
    return render(request, 'new_trip.html', context)

def trip (request, id):
    trip = Trip.objects.get(id=id)
    list_images =json.loads(trip.images.get("images"))
    list_images.reverse()
    if request.method == 'POST' and request.FILES:
        image = request.FILES.get("image")
        if(image.name in list_images):
            result_form = "Ya existe la imagen en el album"
        else:
            images = json.loads(trip.images.get("images"))
            images.append(image.name)
            Trip.objects.update(id=id, images={"images":json.dumps(images)})

            bucket = storage.bucket()
            blob = bucket.blob(f'trips/{request.user}/'+trip.location+"/"+image.name)
            blob.upload_from_file(image) 
            
            result_form = ""   
            return redirect(f"../../trip/{id}")
    else:
        result_form = ""     
   
    context = {
        'trip':trip,
        'images':list_images,
        'result_form': result_form
    }
    return render(request, 'trip.html', context)