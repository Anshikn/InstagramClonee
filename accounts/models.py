from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField()


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=30, blank=True)
  url = models.URLField(blank=True)
  bio = models.TextField(blank=True)
  profile_image = models.ImageField(upload_to='accounts/profile_images', blank=True)