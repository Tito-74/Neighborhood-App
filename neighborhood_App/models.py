from django.db import models
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    hood_photo = CloudinaryField('images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')



class Profile(models.Model):
    profile_pict = CloudinaryField('images')
    bio = models.TextField(max_length = 250, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
