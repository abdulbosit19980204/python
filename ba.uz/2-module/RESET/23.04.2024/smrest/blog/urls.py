from django.urls import path
from .views import PostListAPIView, CategoriesListAPIView, CategoryRetrieveAPIView, CommentPostListAPIView, \
    PostRetrieveAPIView, UserCreateAPIView

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view()),

    path('posts/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),

    path('comments/', CommentPostListAPIView.as_view()),
    path('comments/<int:pk>', CommentPostListAPIView.as_view()),

    path('user/create/', UserCreateAPIView.as_view()),
]
