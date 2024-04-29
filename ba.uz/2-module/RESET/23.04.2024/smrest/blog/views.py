from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post, CommentPost, LikePost, FavoritePost, MyUser, FollowMyUser, Notification, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, MyUserSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentRetriveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer


class CommentPostListAPIView(ListAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUser

    def post(self, request):
        data = request.data
        user = User.objects.create(username=data['username'], email=data['email'],
                                   password=make_password(data['password']))
        user.save()
        data['user'] = user.id
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def home_view(request):
    return Response(
        data={"message": "Hello World!"},
        status=status.HTTP_200_OK
    )
