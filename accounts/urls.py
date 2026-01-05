from django.contrib import admin
from django.urls import path
from .views import ProfileView,RegistrationView,ProfileEditView
# from rest_framework import routers


# routers = routers.DefaultRouter()
# routers.register('profile', ProfileSerializers)


urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/edit/',ProfileEditView.as_view()),

]