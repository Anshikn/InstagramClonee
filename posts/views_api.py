from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializers, FeedPostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from follow_unfollow.models import Follow
from django.db.models import Q

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


class FeedView(ListAPIView):
    serializer_class = FeedPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        following_ids = Follow.objects.filter(follower=user).values_list('following_id', flat=True)
        return Post.objects.filter(
            Q(user__id__in=following_ids) | Q(user=user)
        ).select_related('user').order_by('-created_at')



