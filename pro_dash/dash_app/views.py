# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.views.decorators.csrf import csrf_exempt

from dash_app.forms import ProfileForm
from dash_app.models import Profile



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            print(login(request, user))
            return render(request, 'dash_app/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'dash_app/signup.html', {'form': form})



def home(request):
    return render(request,"dash_app/index.html",{})



def SaveProfile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()

    return render(request, 'saved.html', locals())