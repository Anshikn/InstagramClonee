from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializers
from posts.models import Post


class CommentCreateView(generics.CreateAPIView):
  serializer_class = CommentSerializers
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    post_id = self.kwargs['post_id']
    post = Post.objects.get(id=post_id)
    serializer.save(user=self.request.user, post=post)

class CommentListView(generics.ListAPIView):
  serializer_class = CommentSerializers

  def get_queryset(self):
    post_id = self.kwargs['post_id']
    return Comment.objects.filter(post_id=post_id).order_by('-created_at') 

class DeleteCommentView(generics.DestroyAPIView):
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Comment.objects.filter(user=self.request.user)
