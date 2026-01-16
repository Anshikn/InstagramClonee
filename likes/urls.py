from django.urls import path
from .views_api import LikeToggleAPIView
from .views import toggle_like_view


urlpatterns = [
  path('api/toggle/', LikeToggleAPIView.as_view(),name='like-toggle'),

  #template
  # likes/urls.py


    path('toggle/<int:post_id>/', toggle_like_view, name='toggle-like'),

]
