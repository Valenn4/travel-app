from django.shortcuts import render, redirect
from .forms import FormRegister, FormLogin
from profiles.models import UserProfile
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = FormLogin(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(request, username=form.data['username'], password=form.data['password'])
            auth.login(request, user)
            return redirect("../profile")
        else:
            print(form.errors)
    else:
        form = FormLogin()
    context = {
        'form': form
    }
    return render(request, 'authentication/login.html', context)
def register(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        
        if form.is_valid():
            UserProfile.objects.create_user(
                username=form.data['username'],
                password=form.data['password1'],
                email=form.data['email'],
                first_name=form.data['first_name']
            )
            return redirect("../login")
        else:
            error = ''
            for el in form.errors.as_data().values():
                error = el[0].message
                break
    else:
        form = FormRegister()
        error = ''

    context = {
        'form':form,
        'error':error
    }
    return render(request, 'authentication/register.html', context)