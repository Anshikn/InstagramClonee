from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField()


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  profile_image = models.ImageField(upload_to='accounts/profile_images', blank=True)