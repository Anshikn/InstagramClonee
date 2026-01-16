# comments/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from posts.models import Post


@login_required
def add_comment_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

    return redirect(request.META.get('HTTP_REFERER', 'feed'))

def comment_list_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    form = CommentForm() if request.user.is_authenticated else None

    return render(
        request,
        'comments/comment_list.html',
        {'post': post, 'comments': comments, 'form': form}
    )

@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(
        Comment,
        id=comment_id,
        user=request.user
    )
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'feed'))
