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

    def __str__(self):
        return self.name
        
    def save_neigborhood(self):
        self.save()
    def delete_neigborhood(self):
        self.delete()
    @classmethod
    def find_neigborhood(cls, hood_id):
        return cls.objects.filter(id=hood_id)
    @property
    def occupants_count(self):
        return self.neighbourhood_users.count()
    def update_neigborhood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(max_length = 250, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    profile_pict = CloudinaryField('images')
    

    def __str__(self):
        return self.user.name
    
    