from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
  user = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = Comment
    fields = ['id','user','text','created_at']
    
    read_only_fields = ['id', 'user', 'created_at']
