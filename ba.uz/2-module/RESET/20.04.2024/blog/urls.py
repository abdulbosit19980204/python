from django.urls import path
from .views import (home_view, posts_view, post_detail_view, create_user_view, category_view,
                    category_detail_view, search_view)

urlpatterns = [
    path('', home_view),
    path('categories/', category_view),
    path('categories/<int:category_id>/', category_detail_view),
    path('posts/', posts_view),
    path('posts/<int:pk>', post_detail_view),
    path('users/', create_user_view),
    path('search/', search_view),
]
