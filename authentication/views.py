from django.shortcuts import render, redirect
from .forms import FormRegister
from django.contrib import messages
from django.contrib.auth.views import LoginView
# Create your views here.


class LoginView(LoginView):
    redirect_authenticated_user = True
    
def register(request):
    if request.user.is_authenticated():
        return redirect("../feed")
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message="Usuario creado exitosamente")
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