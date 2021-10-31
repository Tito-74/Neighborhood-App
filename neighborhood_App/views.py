from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .forms import UserRegisterForm
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
        print("form:",form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # print("user:",username)
            messages.success(request,f"Account created for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    
    return render(request,'user/register.html',{'form': form})


def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    return render(request,'profile.html',{"profile":profile})

