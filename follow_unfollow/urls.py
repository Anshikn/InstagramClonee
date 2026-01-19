from django.urls import path
from .views_api import FollowToggleView
from .views import follow_toggle_view

urlpatterns = [
    #api
    path('api/<int:user_id>/toggle/', FollowToggleView.as_view(), name='follow-toggle'),
    #template
    path('toggle/<int:user_id>/', follow_toggle_view, name='toggle-follow'),
]
