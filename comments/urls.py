from django.urls import path
from .views_api import CommentCreateView,CommentListView,DeleteCommentView
from .views import add_comment_view, comment_list_view, delete_comment_view

urlpatterns = [
    #api
    path('api/<int:post_id>/', CommentListView.as_view(), name='comment-list'),
    path('api/<int:post_id>/add/', CommentCreateView.as_view(), name='comment-add'),
    path('api/delete/<int:pk>/', DeleteCommentView.as_view(), name='comment-delete'),
    #template
    path('add/<int:post_id>/', add_comment_view, name='add-comment'),
    path('post/<int:post_id>/', comment_list_view, name='comment-list'),
    path('delete/<int:comment_id>/', delete_comment_view, name='delete-comment'),
]

