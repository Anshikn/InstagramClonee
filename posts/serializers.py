from rest_framework import serializers
from .models import Post
from likes.models import Like

class PostSerializers(serializers.ModelSerializer):
  likes_count = serializers.SerializerMethodField()
  is_liked = serializers.SerializerMethodField()
  comments_count = serializers.SerializerMethodField()


  # user = serializers.ReadOnlyField(source='user.id')
  class Meta:
    model = Post
    fields = [ 'id','caption', 'image', 'created_at', 'likes_count', 'is_liked','comments_count' ]


  def get_likes_count(self, obj):
    return obj.likes.count()
  
  def get_is_liked(self, obj):
    user = self.context['request'].user
    if user.is_anonymous:
      return False
    return obj.likes.filter(user=user).exists()
  
  def get_comments_count(self, obj):
        return obj.comments.count()
  

class FeedPostSerializer(serializers.ModelSerializer):
   username = serializers.ReadOnlyField(source='user.username')
   profile_image = serializers.ImageField(source='user.profile.profile_image',read_only=True)
   likes_count = serializers.SerializerMethodField()
   comments_count = serializers.SerializerMethodField()
   is_liked = serializers.SerializerMethodField()

   class Meta:
      model = Post
      fields = ['id', 'username', 'profile_image', 'caption', 'image', 'created_at', 'likes_count', 'is_liked', 'comments_count']

    
   def get_likes_count(self, obj):
          return obj.likes.count()

   def get_comments_count(self, obj):
          return obj.comments.count()

   def get_is_liked(self, obj):
     request = self.context.get('request')
     if not request or not request.user.is_authenticated:
      return False

     return Like.objects.filter(
              user=request.user,
              posts=obj
          ).exists()