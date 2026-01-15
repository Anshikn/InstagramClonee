from django.urls import path
from .views_api import PostViewSet,FeedView
from rest_framework import routers
from django.conf.urls import include


routers = routers.DefaultRouter()
routers.register('posts',PostViewSet )


urlpatterns = [
    # path('posts/', PostView.as_view()),
    # path('postCreate/', PostCreateView.as_view()),
    path('api/', include(routers.urls)),
    path('feed/', FeedView.as_view()),
    
]