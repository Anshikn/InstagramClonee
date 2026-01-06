from rest_framework import serializers
from .models import Like


class likeSerializers(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = ['id', 'posts','created_at']
    read_only_fields = ['id','created_at']

