from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Business,Neighbourhood

class SignUpForm(UserCreationForm):
    # email = forms.EmailField()

    class meta:
        model = User
        fields = ('username','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        # self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user',]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model=User
        exclude=['user',]

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Post
        template_name = "add.html"
        fields = ['user','title','image','content','neighbourhood']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','neighbourhood','avatar']

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        template_name = "buzpost.html"
        fields = ['user','name','bizzhood','bizz_email','desc']

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        template_name = "buzpost.html"
        fields = ['user','name','bizzhood','bizz_email','desc']


class AddNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        template_name = "neighbourhood.html"
        fields = ['name','hood_location','description','hood_photo']





    