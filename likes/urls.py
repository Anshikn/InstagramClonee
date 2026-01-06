from django.urls import path
from .views import LikeToggleAPIView


urlpatterns = [
  path('toggle/', LikeToggleAPIView.as_view(),name='like-toggle'),

]
