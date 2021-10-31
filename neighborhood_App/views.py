from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import UserRegisterForm, UpdateProfileForm, AddEventForm
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
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
            messages.success(request,f"Account created for {request.user}!")
            return redirect('login')
            
            # return redirect('login')
    else:
        form = UserRegisterForm()

    
    return render(request,'user/register.html',{'form': form})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    return render(request,'user/profile.html',{"profile":profile})

# def update_profilePage(request):

#     return render(request,"user/update.html")

def update_profilePage(request, id):
    # obj = get_object_or_404(Profile, user_id=id)
    obj2 = get_object_or_404(User, id=id)
    form = UpdateProfileForm(request.POST or None, request.FILES)
    # form2 = UpdateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form2.save()
        return HttpResponseRedirect("/profile")

    return render(request,"user/update.html", {"form": form})

def eventPost(request):

    current_user = request.user
    form = AddEventForm()
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            post_event = form.save(commit=False)
            post_event.user = current_user
            post_event.save()
            return redirect('home')
    else:
        form = AddEventForm()
    return render(request,"user/add.html", {'form':form})

def businessView(request):
    return render(request,"index.html")   



