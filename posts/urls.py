from django.urls import path
from .views_api import PostViewSet,FeedView
from rest_framework import routers
from django.conf.urls import include
from . import views

routers = routers.DefaultRouter()
routers.register('posts',PostViewSet )


urlpatterns = [
    # path('posts/', PostView.as_view()),
    # path('postCreate/', PostCreateView.as_view()),
    path('api/', include(routers.urls)),
    path('api/feed/', FeedView.as_view()),

    path('create/', views.create_post_view, name='create-post'),
    path('feed/', views.feed_view, name='feed'),
    path('user/<str:username>/', views.user_posts_view, name='user-posts'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete-post'),
    
]