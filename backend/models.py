from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username


class Item(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_link = models.TextField()
    favorite = models.BooleanField(default=False)
    
    