import json
from django.http import HttpResponse
from django.shortcuts import render
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
    for trip in Trip.objects.filter(user=request.user):
        list_images =json.dumps(json.loads(trip.images).get("images"))[1:-1].replace('"', "").split(", ")
        trips.append({"title": trip.title, "location":trip.location, "images":list_images, "last_image":list_images[len(list_images)-1]})
    context = {
        'trips':trips,
    }
    return render(request, 'profile.html', context)

def new_trip(request):
    if request.method=='POST' and request.FILES.get("image"):
        form = FormNewTravel(request.POST)
        images = {"images":[]}
        for image in request.FILES.getlist("image"):
            bucket = storage.bucket()
            blob = bucket.blob(f'trips/{request.user}/'+form.data["location"]+"/"+image.name)
            blob.upload_from_file(image)
            images.get("images").append(image.name)
        
        if(Trip.objects.filter(user = request.user,title=form.data["title"]).exists()):
            new_images = Trip.objects.get(user = request.user,title=form.data["title"]).images
            new_images_json = json.loads(new_images)
            for el in images.get("images"):
                if not el in new_images_json.get("images"):
                    new_images_json.get("images").append(el)

            Trip.objects.update(
                user = request.user,
                title=form.data["title"],
                images=json.dumps(new_images_json)
            )
        else:
            Trip.objects.create(
                user = request.user,
                location = form.data["location"],
                title = form.data["title"],
                images = json.dumps(images)
            )
    else:
        form = FormNewTravel()

    
    context={
        "form":form,
    }
    return render(request, 'new_trip.html', context)