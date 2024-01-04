from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, reverse
from .models import MyUser
from users.forms import UserLoginForm, UserRegistrationForm, UserProfile
from django.contrib import auth

def reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("log")
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "users/register.html", context)

def log(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('photorate:photo_rate'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, "users/login.html", context)

def profile(request):
    if request.method == 'POST':
        form = UserProfile(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("profile")
        else:
            print(form.errors)
    else:
        form = UserProfile(instance=request.user)
    context = {'form': form}
    return render(request,"users/profile.html", context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('photorate:photo_rate')
