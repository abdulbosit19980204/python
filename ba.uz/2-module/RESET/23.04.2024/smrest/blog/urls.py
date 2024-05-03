from django.urls import path
from .views import (CategoriesListAPIView, CategoryRetrieveAPIView, CategoriesCreateAPIView, PostListAPIView,
                    PostRetrieveAPIView, PostRetriveEditAPIView, PostCreateAPIView, CommentCreateAPIView,
                    CommentPostListAPIView,
                    FollowMyUserAPIView, FollowCreateAPIView, LikePostListAPIView, LikeCreateAPIView,
                    )

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    path('categories/create/', CategoriesCreateAPIView.as_view()),

    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>', PostRetrieveAPIView.as_view()),
    path('posts/edit/<int:pk>/', PostRetriveEditAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),

    path('comments/', CommentPostListAPIView.as_view()),
    path('comments/<int:pk>', CommentPostListAPIView.as_view()),
    path('comments/create/', CommentCreateAPIView.as_view()),

    path('followers/', FollowMyUserAPIView.as_view()),
    path('follow/create/', FollowCreateAPIView.as_view()),

    path('like/', LikePostListAPIView.as_view()),
    path('like/create/', LikeCreateAPIView.as_view()),

]
