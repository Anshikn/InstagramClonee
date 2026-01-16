# likes/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Like
from posts.models import Post

@login_required
def toggle_like_view(request, post_id):
    """
    Template equivalent of LikeToggleAPIView
    """
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        posts=post
    )

    # If already liked → unlike
    if not created:
        like.delete()

    # Redirect back to previous page (feed / profile)
    return redirect(request.META.get('HTTP_REFERER', 'feed'))
