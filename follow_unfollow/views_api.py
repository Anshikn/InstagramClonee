from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Follow



User = get_user_model()

class FollowToggleView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request, user_id):
    if request.user.id == user_id:
      return Response({
        "detail": "You can't follow yourself"
      },
      status=status.HTTP_400_BAD_REQUEST
      )
    user_to_follow = User.objects.get(id = user_id)

    follow, created = Follow.objects.get_or_create(
      follower = request.user,
      following = user_to_follow
    )

    if not created:
      follow.delete()
      return Response({"following":False})
    
    return Response({"following":True})

