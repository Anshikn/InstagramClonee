from django.urls import path
from .views import CommentCreateView,CommentListView,DeleteCommentView

urlpatterns = [
    path('<int:post_id>/', CommentListView.as_view(), name='comment-list'),
    path('<int:post_id>/add/', CommentCreateView.as_view(), name='comment-add'),
    path('delete/<int:pk>/', DeleteCommentView.as_view(), name='comment-delete'),
]
