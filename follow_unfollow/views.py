# follows/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Follow

User = get_user_model()

@login_required
def follow_toggle_view(request, user_id):
    if request.user.id == user_id:
        return redirect('profile')

    user_to_follow = get_object_or_404(User, id=user_id)

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if not created:
        follow.delete()

    return redirect(request.META.get('HTTP_REFERER', 'profile'))
