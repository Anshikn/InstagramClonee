from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
  likes_count = serializers.SerializerMethodField()
  is_liked = serializers.SerializerMethodField()

  # user = serializers.ReadOnlyField(source='user.id')
  class Meta:
    model = Post
    fields = [ 'id','caption', 'image', 'created_at', 'likes_count', 'is_liked' ]


  def get_likes_count(self, obj):
    return obj.likes.count()
  
  def get_is_liked(self, obj):
    user = self.context['request'].user
    if user.is_anonymous:
      return False
    return obj.likes.filter(user=user).exists()
