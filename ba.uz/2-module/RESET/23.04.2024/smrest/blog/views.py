from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Post, CommentPost, LikePost, FavoritePost, MyUser, FollowMyUser, Notification, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, MyUserSerializer
from .mixins import CreateDeleteUpdateAPIView


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    # Look up field lar qayerdan va qaysi nom bilan kelgan qiymatni qidirish kerak ligini korsatadi
    # lookup_field = 'id'
    # lookup_url_kwarg = 'pq'
    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        return super().retrieve(request, *args, **kwargs)


class CategoriesCreateAPIView(CreateAPIView):
    queryset = Category
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        user = MyUser.objects.filter(user_id=request.user.id).first()
        data = request.data
        category = Category.objects.create(name=data['name'], author=user, is_active=False)
        category.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "category": "CategorySerializer(category)"
            }

        )


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        user = MyUser.objects.filter(user_id=request.user.id).first()
        data = request.data
        post = Post.objects.create(author=user, title=data['title'], content=data['content'],
                                   post_image=data['post_image'])
        post.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "data": PostSerializer(post).data
            }
        )


class PostRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]


class CommentRetriveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]


class CommentPostListAPIView(ListCreateAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]


class LikePostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]


class LikeCreateAPIView(CreateAPIView):
    queryset = LikePost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        user = MyUser.objects.filter(user_id=request.user.id).first()
        post = Post.objects.filter(id=request.data.get('post_id')).first()
        is_liked = LikePost.objects.filter(author=user, post=post).first()
        if not is_liked:
            likedPost = LikePost.objects.create(author=user, post=post)
            likedPost.save()
            post.like_count += 1
            post.save(update_fields=['like_count'])
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "data": PostSerializer(post).data
                }
            )
        else:
            data = is_liked
            is_liked.delete()
            post.like_count -= 1
            post.save(update_fields=['like_count'])
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": PostSerializer(post).data,
                    "message": "unliked"
                }

            )


class LikePostRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]


class FollowMyUserAPIView(CreateAPIView):
    queryset = FollowMyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthenticated, ]


class FollowCreateAPIView(CreateAPIView):
    queryset = FollowMyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        print(request.data.get('following_id'))
        follower = MyUser.objects.filter(user_id=request.user.id).first()
        following = MyUser.objects.filter(user_id=request.data.get('following_id')).first()

        is_followed = FollowMyUser.objects.filter(follower=follower, following=following).first()
        if not is_followed:
            follow = FollowMyUser.objects.create(follower=follower, following=following)
            follow.save()

            follower.following_count += 1
            following.follower_count += 1
            follower.save(update_fields=['following_count'])
            following.save(update_fields=['follower_count'])

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "follower": MyUserSerializer(follower).data,
                    "following": MyUserSerializer(following).data,
                    "status": "Followed"
                }
            )
        else:
            is_followed.delete()
            follower.following_count -= 1
            following.follower_count -= 1
            follower.save(update_fields=['following_count'])
            following.save(update_fields=['follower_count'])

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "follower": MyUserSerializer(follower).data,
                    "following": MyUserSerializer(following).data,
                    "status": "Followed"
                }
            )


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
