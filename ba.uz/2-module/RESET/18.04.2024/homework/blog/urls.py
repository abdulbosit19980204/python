from django.urls import path
from .views import home_view, posts_view, post_detail_view, comment_view, comments_view, search_view

urlpatterns = [
    path('', home_view),
    path('posts/', posts_view),
    path('post/<int:pk>/', post_detail_view),
    path('comments/', comments_view),
    path('comment/<int:pk>/', comment_view),
    path('search/', search_view),

]
