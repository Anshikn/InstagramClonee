from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Like
from posts.models import Post



class LikeToggleAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    post_id = request.data.get('post')
    
    if not post_id:
      return Response({
        "detail": "Post id is required"
      },
      status=status.HTTP_400_BAD_REQUEST
      )
    
    post = Post.objects.get(id=post_id)

    like,created = Like.objects.get_or_create(
      user = request.user,
      posts = post
    )

    if not created:
      like.delete()
      return Response({"liiked":False})
    
    return Response({"liked":True})

    