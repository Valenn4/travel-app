from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormNewTravel
import cloudinary
from cloudinary import uploader, Search, api
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
    if request.method=='POST':
        form = FormNewTravel(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get("image")
            bucket = storage.bucket()
            blob = bucket.blob('users/Valenn2003/'+file.name)
            blob.upload_from_file(file)
    else:
        form = FormNewTravel()
    context={
        "form":form,
    }
    return render(request, 'profile.html', context)