from django.shortcuts import render
from .forms import FormNewTravel
import cloudinary
from cloudinary import uploader, Search, api
# Create your views here.

def profile(request):
    if request.method=='POST':
        form = FormNewTravel(request.POST, request.FILES)
        if form.is_valid():
            cloudinary.uploader.upload(form.cleaned_data.get("image"), 
            public_id = form.data["title"], folder=f"trips/Valenn2003/{form.data['location']}")
    else:
        form = FormNewTravel()


    resources = cloudinary.api.resources(type='upload', prefix="users/Valenn4")
    image_profile = resources['resources'][0]["url"]
    context={
        "form":form,
        'image_profile':image_profile,
    }
    return render(request, 'profile.html', context)