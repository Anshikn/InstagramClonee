# views.py (template views)
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileEditForm
from follow_unfollow.models import Follow
from django.contrib.auth import get_user_model

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
# def profile_view(request):
#     profile, created = Profile.objects.get_or_create(user=request.user)
#     return render(request, 'accounts/profile.html', {'profile': profile})
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    is_following = False
    if request.user != profile.user:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile.user
        ).exists()

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'is_following': is_following
    })

@login_required
def edit_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save(user=request.user)
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

# @login_required
# def users_list_view(request):
#     users = User.objects.exclude(id=request.user.id)
#     return render(request, 'accounts/users_list.html', {'users': users})

@login_required
def users_list_view(request):
    users = User.objects.exclude(id=request.user.id)

    following_ids = request.user.following.values_list(
        'following_id', flat=True
    )

    return render(request, 'accounts/users_list.html', {
        'users': users,
        'following_ids': following_ids,
    })
