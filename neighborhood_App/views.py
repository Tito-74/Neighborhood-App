from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import UserRegisterForm, UpdateProfileForm, AddEventForm,AddBusinessForm,AddNeighbourhoodForm
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    hood = Neighbourhood.objects.all()
    context={'posts':posts, 'hood':hood}
    return render(request,"index.html",context)
   
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

def update_profilePage(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form = UpdateProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('profile')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = UpdateProfileForm(instance=profile)
    else:
        form = UpdateProfileForm()


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
    business = Business.objects.all()
    context = {'business': business}
    return render(request,"user/business.html", context )   

def viewEvents(request, id):
    post = Post.objects.get(id=id)

    return render(request,"user/event.html",{'post':post}) 

def addBuzpost(request):

    current_user = request.user
    form = AddBusinessForm()
    if request.method == 'POST':
        form = AddBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            post_event = form.save(commit=False)
            post_event.user = current_user
            post_event.save()
            return redirect('home')
    else:
        form = AddBusinessForm()
    return render(request,"user/buzpost.html", {'form':form})

def addNeighbourhood(request):

    current_user = request.user
    form = AddNeighbourhoodForm()
    if request.method == 'POST':
        form = AddNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            post_event = form.save(commit=False)
            post_event.user = current_user
            post_event.save()
            return redirect('home')
    else:
        form = AddNeighbourhoodForm()
    return render(request,"user/neighbourhood.html", {'form':form})

