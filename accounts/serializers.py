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

class ProfileEditUserSerializers(serializers.ModelSerializer):
  username = serializers.CharField(required=False, allow_blank=False)
  class Meta:
    model = User
    fields = ['username']

class ProfileSerializers(serializers.ModelSerializer):

  bio = serializers.CharField(required=False, allow_blank=True)
  profile_image = serializers.ImageField(required=False, allow_null=True)
  user_name = ProfileEditUserSerializers( source='user',
        required=False)
  followers_count = serializers.SerializerMethodField()
  following_count = serializers.SerializerMethodField()
  is_following = serializers.SerializerMethodField()

  class Meta:
    model = Profile
    fields = ['bio','profile_image','first_name','user_name','url','followers_count','following_count','is_following']    


  def get_followers_count(self, obj):
        return obj.user.followers.count()

  def get_following_count(self, obj):
        return obj.user.following.count()

  def get_is_following(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return obj.user.followers.filter(follower=user).exists()


class ProfileEditSerializers(serializers.ModelSerializer):

  user_name = ProfileEditUserSerializers( source='user',
        required=False)
  bio = serializers.CharField(required=False, allow_blank=True)
  profile_image = serializers.ImageField(required=False, allow_null=True)
  

  class Meta:
    model = Profile
    fields = ['user_name','first_name','last_name','bio','profile_image','url']

  #updating profile user 
  def update(self, instance, validated_data):
    user_data = validated_data.pop('user', None)
    
    if user_data:
            user = instance.user
            username = user_data.get('username', None)

            # update ONLY if provided and not empty
            if username:
                user.username = username
                user.save()

        # ✅ PROFILE UPDATE
    for attr, value in validated_data.items():
      setattr(instance, attr, value)

    instance.save()
    return instance