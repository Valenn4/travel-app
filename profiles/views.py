import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormNewTravel, FormChangeUser, FormAddImage, FormNewMessage
from chat.forms import FormNewLivingRoom
from .models import Trip, UserProfile, Publication
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

def get_image_trip(request, title, image, user):
    bucket = storage.bucket()
    blob = bucket.blob(f"trips/{user}/{title}/{image}")
    
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
    if request.method == 'POST':
        if 'form_new_message' in request.POST:
            form_new_message = FormNewMessage(request.POST)
            if form_new_message.is_valid():
                Publication.objects.create(
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
                    blob = bucket.blob(f'trips/{request.user}/'+form_new_trip.data["title"]+"/"+image.name)
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
        if 'form_new_livingroom' in request.POST:
            form_new_livingroom = FormNewLivingRoom(request.POST)    
            
            name = form_new_livingroom.data["name"]
            nacionality = form_new_livingroom.data["nacionality"]

            LivingRoom.objects.create(created_by=request.user, name=name, nacionality=nacionality)

            return redirect("../feed")
        form_new_livingroom = FormNewLivingRoom()    
        form_new_message = FormNewMessage()
        form_new_trip = FormNewTravel()
    else:
        form_new_message = FormNewMessage()
        form_new_trip = FormNewTravel()
    user = UserProfile.objects.get(username=user)
    # TRIPS
    trips = []
    for trip in Trip.objects.filter(user=user).order_by("-id"):
        list_images = json.loads(trip.images.get("images"))
        trips.append({"id": trip.id, "title": trip.title, "location":trip.location, "images":list_images, "last_image":list_images[len(list_images)-1]})
    # MESSAGGES
    messages = Publication.objects.filter(user=user).order_by("-id")
    context = {
        'is_following': request.user.following["followings"],
        'user_profile': user,
        'trips':trips,
        'list_messages': Publication.objects.filter(user=user).order_by("-id"),
        'form_new_message': form_new_message,
        'form_new_trip': form_new_trip,
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
        if(request.FILES.get("image_profile") != None and request.user.image_profile != ''):
            image_last = bucket.blob(f'users/{request.user}/{request.user.image_profile}')
            image_last.delete()
            user.image_profile = request.FILES.get("image_profile").name
            blob = bucket.blob(f'users/{request.user}/'+request.FILES.get("image_profile").name)
            blob.upload_from_file(request.FILES.get("image_profile"))
        elif(request.FILES.get("image_profile") != None and request.user.image_profile == ''):
            user.image_profile = request.FILES.get("image_profile").name
            blob = bucket.blob(f'users/{request.user}/'+request.FILES.get("image_profile").name)
            blob.upload_from_file(request.FILES.get("image_profile"))
        
        if(request.FILES.get("image_portate") != None and request.user.image_portate != ''):
            image_last = bucket.blob(f'portate/{request.user}/{request.user.image_portate}')
            image_last.delete()
            user.image_portate = request.FILES.get("image_portate").name
            blob = bucket.blob(f'portate/{request.user}/'+request.FILES.get("image_portate").name)
            blob.upload_from_file(request.FILES.get("image_portate"))
        elif(request.FILES.get("image_portate") != None and request.user.image_portate == ''):
            user.image_portate = request.FILES.get("image_portate").name
            blob = bucket.blob(f'portate/{request.user}/'+request.FILES.get("image_portate").name)
            blob.upload_from_file(request.FILES.get("image_portate"))
        user.save()
    
        return redirect(f'../../profile/{request.user.username}')
    else:
        form = FormChangeUser(instance = request.user)
    context = {
        'user': UserProfile.objects.get(id=request.user.id),
        'form': form,
        'countries': rapi.get_all()
    }
    return render(request, 'profile/edit_profile.html', context)

@login_required(redirect_field_name=None)
def trip (request, id):
    trip = Trip.objects.get(id=id)
    list_images =json.loads(trip.images.get("images"))
    if request.method == 'POST':
        if 'submit_delete_photo' in request.POST:
            if len(list_images) == 1:
                error_delete = 'El album no puede quedar vacio',
            else:
                images = list_images
                images.remove(request.POST["name_image"])
                trip.images = {"images":json.dumps(images)}
                trip.save()
                bucket = storage.bucket()
                blob = bucket.blob(f'trips/{request.user}/'+trip.title+"/"+request.POST["name_image"])
                blob.delete()
                result_form = ''
                error_delete = ''
        elif 'submit_delete_album' in request.POST:
            bucket = storage.bucket()
            blobs = bucket.list_blobs(prefix = f'trips/{request.user}/'+trip.title+"/")
            for blob in blobs:
                blob.delete()
            trip.delete()
            return redirect(f'../../profile/{request.user.username}')
        else:
            form = FormAddImage(request.POST, request.FILES)
            result_form = []
            for image in request.FILES.getlist("image"):
                if(image.name in list_images):
                    result_form.append(image.name)
                else:
                    images = json.loads(trip.images.get("images"))
                    images.append(image.name)
                    
                    trip.images = {"images":json.dumps(images)}
                    trip.save()
                    bucket = storage.bucket()
                    blob = bucket.blob(f'trips/{request.user}/'+trip.title+"/"+image.name)
                    blob.upload_from_file(image)
                    list_images.append(image.name)
        form = FormAddImage(request.POST, request.FILES)
        error_delete = ''
    else:
        form = FormAddImage(request.POST)
        result_form = ""     
        error_delete = ''
    list_images.reverse()

    '''WEB'''
    list_images_copy_web = list_images
    group_images_web = [[],[],[],[]]
    while len(list_images_copy_web) != 0:
        if len(list_images_copy_web)<4:
            for i in range(len(list_images_copy_web)):
                list_modify = group_images_web[i]
                list_modify.append(list_images_copy_web[i])
                group_images_web[i] = list_modify
            list_images_copy_web = []
        else:
            for i in range(4):
                list_modify = group_images_web[i]
                list_modify.append(list_images_copy_web[i])
                group_images_web[i] = list_modify
            list_images_copy_web = list_images_copy_web[4::]
    
    '''MOBILE'''
    list_images_copy_mobile = list_images
    group_images_mobile = [[],[]]
    while len(list_images_copy_mobile) != 0:
        if len(list_images_copy_mobile)<2:
            for i in range(len(list_images_copy_mobile)):
                list_modify = group_images_mobile[i]
                list_modify.append(list_images_copy_mobile[i])
                group_images_mobile[i] = list_modify
            list_images_copy_mobile = []
        else:
            for i in range(2):
                list_modify = group_images_mobile[i]
                list_modify.append(list_images_copy_mobile[i])
                group_images_mobile[i] = list_modify
            list_images_copy_mobile = list_images_copy_mobile[2::]

    context = {
        'trip':trip,
        'list_images_web':group_images_web,
        'list_images_mobile': group_images_mobile,
        'result_form': result_form,
        'form': form,
        'user_trip': Trip.objects.get(id=id).user.username,
        'error_delete':error_delete
    }
    return render(request, 'profile/trip.html', context)
