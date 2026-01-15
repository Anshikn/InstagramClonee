# views.py (template views)
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileEditForm


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
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

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