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

class ProfileEditUserSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username']

class ProfileEditSerializers(serializers.ModelSerializer):

  user_name = ProfileEditUserSerializers( source='user',
        required=False)
  bio = serializers.CharField(required=False, allow_blank=True)
  profile_image = serializers.ImageField(required=False, allow_null=True)
  

  class Meta:
    model = Profile
    fields = ['bio','profile_image','user_name']

  #updating profile user 
  def update(self, instance, validated_data):
    user_data = validated_data.pop('user', None)
    if user_data:
      user = instance.user
      for attr, value in user_data.items():
        setattr(user, attr, value)
      user.save() 
    #updating profile models values  over rided
    for attr, value in validated_data.items():
      setattr(instance, attr, value)

    instance.save()
    return instance