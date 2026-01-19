from django.contrib import admin
from django.urls import path
from .views_api import ProfileView,RegistrationView,ProfileEditView
# from rest_framework import routers
from django.contrib.auth import views as auth_views
from . import views


# routers = routers.DefaultRouter()
# routers.register('profile', ProfileSerializers)


urlpatterns = [
    #api urls
    path('api/registration/', RegistrationView.as_view()),
    path('api/profile/', ProfileView.as_view()),
    path('api/profile/edit/',ProfileEditView.as_view()),

    #template urls
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('users/', views.users_list_view, name='users-list'),


]