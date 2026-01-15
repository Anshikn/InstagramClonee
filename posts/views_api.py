from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializers
from .models import Post
from .permissions import IsAuthorOrReadOnly


# Create your views here.

# class PostView(generics.ListAPIView):
#   queryset = Post.objects.all().order_by('-created_at')
#   serializer_class = PostSerializers

# class PostCreateView(generics.CreateAPIView):
#   queryset = Post.objects.all() 
#   serializer_class = PostSerializers

#   def perform_create(self, serializer):
#       serializer.save(user=self.request.user)


class PostViewSet(ModelViewSet):
  queryset = Post.objects.all().order_by('-created_at')
  serializer_class = PostSerializers
  permission_classes = [IsAuthorOrReadOnly]
  
  # def get_queryset(self):
  #       return Post.objects.all().order_by('-created_at')

  def perform_create(self, serializer):
        serializer.save(user=self.request.user)
