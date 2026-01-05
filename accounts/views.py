from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ProfileSerializers, RegisterationSerializers
from .models import Profile, User


class RegistrationView(generics.CreateAPIView):
  serializer_class = RegisterationSerializers
  queryset = User.objects.all()
  permission_classes = [AllowAny]

class ProfileView(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializers
  permission_classes = [IsAuthenticated]

  def get_object(self):
    profile, created = Profile.objects.get_or_create(user=self.request.user)
    return profile

