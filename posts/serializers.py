from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):

  # user = serializers.ReadOnlyField(source='user.id')
  class Meta:
    model = Post
    fields = [ 'id','caption', 'image', 'created_at']


