from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileForm
from .models import *

# Create your views here.

def index(request):
    return render(request,"index.html")
   
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print('user:',user)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,"user/login.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            print("user:",user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,f"Account created for {username}!")
            return redirect('login')
            
            # return redirect('login')
    else:
        form = UserRegisterForm()

    
    return render(request,'user/register.html',{'form': form})


def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    return render(request,'user/profile.html',{"profile":profile})



# def user_profile(request,username):
#     user = User.objects.get(username=username)
#     profile =Profile.objects.get(username=user)

#     return render(request,'user/profile.html',{"profile":profile})

def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'user/create_profile.html',{"form":form})  

