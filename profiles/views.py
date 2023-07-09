import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormNewTravel
from .models import Trip, UserProfile
from firebase_admin import storage
# Create your views here.

def get_image(request, image):
    bucket = storage.bucket()
    blob = bucket.blob("users/Valenn2003/"+image)
    
    try:
        image_data = blob.download_as_bytes()
        return HttpResponse(image_data, content_type='image/jpg')  # Cambia el tipo de contenido según tus necesidades
    except Exception as e:
        return HttpResponse('Error al obtener la imagen: {}'.format(str(e)))


def profile(request):
    return render(request, 'profile.html')

def new_trip(request):
    if request.method=='POST' and request.FILES.get("image"):
        form = FormNewTravel(request.POST)
        images = {"images":[]}
        for image in request.FILES.getlist("image"):
            bucket = storage.bucket()
            blob = bucket.blob('trips/Valenn2003/'+form.data["location"]+"/"+image.name)
            blob.upload_from_file(image)
            images.get("images").append(image.name)
        
        if(Trip.objects.filter(user = UserProfile.objects.get(id=1),title=form.data["title"]).exists()):
            new_images = Trip.objects.get(user = UserProfile.objects.get(id=1),title=form.data["title"]).images
            new_images_json = json.loads(new_images)
            for el in images.get("images"):
                new_images_json.get("images").append(el)

            Trip.objects.update(
                user = UserProfile.objects.get(id=1),
                title=form.data["title"],
                images=json.dumps(new_images_json)
            )
        else:
            Trip.objects.create(
                user = UserProfile.objects.get(id=1),
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