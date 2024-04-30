# Auth App URLs

from django.urls import path

from .views import signin_view, logout_view, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signin/', signin_view, name='signin', ),
    path('register/', UserCreateAPIView.as_view()),
    path('logout/', logout_view, name='logout'),

    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
