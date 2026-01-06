from django.db import models
from django.conf import settings

class Post(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  caption = models.TextField(blank = True)
  image = models.ImageField(upload_to='posts/images')
  created_at = models.DateTimeField(auto_now_add=True)
