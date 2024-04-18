from django.urls import path
from .views import post_detail_view, posts_view, comments_view

urlpatterns = [
    path('post-detail/<int:pk>', post_detail_view),
    path('posts/', posts_view),
    path('comments/', comments_view)
]
