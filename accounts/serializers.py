from rest_framework import serializers
from .models import Profile, User



class RegisterationSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'password']

  def create(self, validated_data):
    user = User(  
      username = validated_data['username'],
      email = validated_data['email'],
      is_active = True
      )  
    user.set_password(validated_data['password'])
    user.save()
    return user

class ProfileSerializers(serializers.ModelSerializer):

  bio = serializers.CharField(required=False, allow_blank=True)
  profile_image = serializers.ImageField(required=False, allow_null=True)

  class Meta:
    model = Profile
    fields = ['bio','profile_image']    
