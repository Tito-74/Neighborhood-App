from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import SignUpForm, UpdateProfileForm,UpdateUserForm, AddEventForm,AddBusinessForm,AddNeighbourhoodForm
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
    return render(request,"registration/login.html")

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            print("user:",user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:

        form = SignUpForm()


    return render(request,'registration/register.html', {'form': form})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id).all
    posts = Post.objects.filter(user=current_user.id).all

    return render(request,'registration/profile.html',{"profile":profile, "posts": posts})



def update_profilePage(request, id):

    obj = get_object_or_404(Profile, user_id=id)
    obj2 = get_object_or_404(User, id=id)
    form = UpdateProfileForm(request.POST or None, request.FILES, instance=obj)
    form2 = UpdateUserForm(request.POST or None, instance=obj2)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect("/profile")
    else:
        form = UpdateProfileForm()

  
    return render(request,"registration/update.html", {"form":form,'form2':form2})

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
    return render(request,"registration/add.html", {'form':form})

def businessView(request):
    business = Business.objects.all()
    context = {'business': business}
    return render(request,"registration/business.html", context )   

def viewEvents(request, id):
    hood = Neighbourhood.objects.get(id=id)
    posts = Post.objects.all()

    return render(request,"registration/event.html",{'hood':hood, 'posts':posts}) 

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
    return render(request,"registration/buzpost.html", {'form':form})

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
    return render(request,"registration/neighbourhood.html", {'form':form})


def search(request):
    if 'business' in request.GET and request.GET['business']:
        business = request.GET.get("business")
        results = Business.search_business(business)
        message = f'business'
        return render(request, 'registration/search.html', {'business': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'registration/search.html', {'message': message})

    

