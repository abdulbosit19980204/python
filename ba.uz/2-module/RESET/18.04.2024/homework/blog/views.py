from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post, Comment, Author

from .handlers.sequalizers import sequalizers_post, sequalizers_comment


@api_view(http_method_names=['GET'])
def home_view(request):
    return Response(
        status=status.HTTP_200_OK,
        data={
            "author": "Abdulbosit",
            "active-api": {
                "posts": "api/v1/posts",
                "post-detail": "api/v1/post/<int:pk>/",
                "comments": "api/v1/comments/",
                "comment-detail": "api/v1/comments/<int:pk>/",
                "author": "api/v1/author/",
                "author-detail": "api/v1/author/<int:pk>/",
                "search": "api/v1/search/",
                "categories": "api/v1/categories/",
            }
        }
    )


@api_view(http_method_names=['GET'])
def posts_view(request):
    posts = Post.objects.filter(is_published=True)

    return Response(
        status=status.HTTP_200_OK,
        data={"message": sequalizers_post(posts, many=True)}
    )


@api_view(http_method_names=['GET'])
def post_detail_view(request, pk):
    post_detail = Post.objects.filter(id=pk, is_published=True).first()
    return Response(
        status=status.HTTP_200_OK,
        data={"message": sequalizers_post(post_detail, many=False)}
    )


@api_view(http_method_names=['GET'])
def comments_view(request):
    comments = Comment.objects.all()
    return Response(
        status=status.HTTP_200_OK,
        data={"message": sequalizers_comment(comments, many=True)}
    )


@api_view(http_method_names=['GET'])
def comment_view(request, pk):
    comments = Comment.objects.filter(id=pk, is_published=True).first()
    return Response(
        status=status.HTTP_200_OK,
        data={"message": sequalizers_comment(comments, many=False)}
    )


@api_view(http_method_names=['GET'])
def search_view(request, keywoard):
    post = Post.objects.filter(Q(title__icontains=keywoard) | Q(description__icontains=keywoard))
    if post:
        return Response(
            status=status.HTTP_200_OK,
            data={"message": sequalizers_post(post, many=True)}
        )
    return Response(
        status=status.HTTP_404_NOT_FOUND,
        data={"message": "There are no posts"}
    )


@api_view(http_method_names=['GET'])
def category_view(request, pk):
    posts = Post.objects.filter(category_id=pk, is_published=True)
    if posts:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "category": sequalizers_post(posts, many=True)[0]["category"],
                "message": sequalizers_post(posts, many=True)
            })

    return Response(
        status=status.HTTP_404_NOT_FOUND,
        data={"message": "There are no posts"}
    )
