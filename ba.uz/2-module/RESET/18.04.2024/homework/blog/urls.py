from django.urls import path
from .views import home_view, posts_view, post_detail_view, comment_view, comments_view, search_view, category_view

urlpatterns = [
    path('', home_view),
    path('posts/', posts_view),
    path('post/<int:pk>/', post_detail_view),
    path('comments/', comments_view),
    path('comment/<int:pk>/', comment_view),
    path('categories/', search_view),
    path('category/<int:pk>/', category_view),
    path('search/<str:keywoard>', search_view),

]
