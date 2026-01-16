# posts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreateForm
from follow_unfollow.models import Follow
from django.db.models import Q

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostCreateForm()

    return render(request, 'posts/create_post.html', {'form': form})

# @login_required
# def feed_view(request):
#     user = request.user

#     following_ids = Follow.objects.filter(
#         follower=user
#     ).values_list('following_id', flat=True)

#     posts = Post.objects.filter(
#         Q(user__id__in=following_ids) | Q(user=user)
#     ).select_related('user').order_by('-created_at')

#     return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def feed_view(request):
    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list('following_id', flat=True)

    posts = Post.objects.filter(
        Q(user__id__in=following_ids) | Q(user=request.user)
    ).select_related('user').prefetch_related('likes', 'comments').order_by('-created_at')

    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def user_posts_view(request, username):
    posts = Post.objects.filter(
        user__username=username
    ).order_by('-created_at')

    return render(request, 'posts/user_posts.html', {'posts': posts})

@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('profile')
