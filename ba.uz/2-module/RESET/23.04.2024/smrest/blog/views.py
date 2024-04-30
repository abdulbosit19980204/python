from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post, CommentPost, LikePost, FavoritePost, MyUser, FollowMyUser, Notification, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, MyUserSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class CategoriesListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CategoryRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Look up field lar qayerdan va qaysi nom bilan kelgan qiymatni qidirish kerak ligini korsatadi
    # lookup_field = 'id'
    # lookup_url_kwarg = 'pq'
    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        return super().retrieve(request, *args, **kwargs)


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentRetriveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer


class CommentPostListAPIView(ListCreateAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def home_view(request):
    return Response(

        data={
            "admin": "admin/",
            "auth/": "api/v1/auth/",
            "categories": "api/v1/categories/",
            "retrive_categories": "api/v1/categories/<int:pk>",
        },
        status=status.HTTP_200_OK
    )
