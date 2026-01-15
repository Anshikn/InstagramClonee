# forms.py
from django import forms
from .models import User, Profile 

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        required=False,
        max_length=150
    )

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'bio',
            'profile_image',
            'url',
        ]

    def save(self, user, commit=True):
        profile = super().save(commit=False)

        # 🔁 serializer.update(): user_data handling
        username = self.cleaned_data.get('username')
        if username:
            user.username = username
            user.save()

        if commit:
            profile.save()

        return profile
