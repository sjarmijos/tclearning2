from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from gestion.models import *

# Create your views here.


def register(request):
    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
            return redirect('login')
            
    else:
        form=UserRegisterForm()
    
    return render(request, 'registration/registro.html', {
        'form':form 
    })
