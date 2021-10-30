from django.db import models
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    profile_pict = CloudinaryField('images')
    bio = models.TextField(max_length = 250, blank=True)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
