# from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

from blog.models import Post, Comment
from .post_serialayzer import data_serialize, commets_serialize


# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def post_detail_view(request, pk):
    post = Post.objects.filter(pk=pk).first()
    comments = commets_serialize(Comment.objects.filter(post=post))

    print(comments)
    return Response(
        status=status.HTTP_200_OK,
        data=data_serialize(post, many=False, comments=comments),
    )


@api_view(http_method_names=['GET', 'POST'])
def posts_view(request):
    posts = Post.objects.all()
    return Response(
        status=status.HTTP_200_OK,
        data=data_serialize(posts, many=True),
    )


@api_view(http_method_names=['GET', 'POST'])
def comments_view(request):
    comments = Comment.objects.all()
    return Response(
        status=status.HTTP_200_OK,
        data=commets_serialize(comments),
    )
