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
            "posts": "api/v1/posts",
            "post-detail": "api/v1/post/<int:pk>/",
            "comments": "api/v1/comments/",
            "comment-detail": "api/v1/comments/<int:pk>/",
            "author": "api/v1/author/",
            "author-detail": "api/v1/author/<int:pk>/",
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
def search_view(request):
    pass
