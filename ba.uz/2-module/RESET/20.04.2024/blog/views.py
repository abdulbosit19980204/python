from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import MyUser, Comment, Post, Category
from .serializers import PostSerializer, MyUserSerializer, CommentSerializer, CategorySerializer


@api_view(['GET'])
def home_view(request):
    return Response(
        status=status.HTTP_200_OK,
        data={'title': 'Home', 'content': 'Home Page'}
    )


@api_view(['GET'])
def category_view(request):
    cat = Category.objects.all()
    categories = CategorySerializer(cat, many=True)

    return Response(categories.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_view(request, category_id):
    cat = Category.objects.filter(id=category_id).first()
    posts = Post.objects.filter(category_id=cat.id)

    categories = CategorySerializer(cat)
    posts = PostSerializer(posts, many=True)

    return_data = {'categories': categories.data, 'posts': posts.data}
    return Response(return_data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_user_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_detail_view(request, pk):
    if request.method == 'GET':
        post = Post.objects.filter(pk=pk, is_published=True).first()
        comments = Comment.objects.filter(post_id=post.id)

        post_serializer = PostSerializer(post)
        comment_serializer = CommentSerializer(comments, many=True)

        response_data = {
            'post': post_serializer.data,
            'comments': comment_serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_view(request):
    if request.method == 'GET':
        keywords = request.query_params.get('keywords')
        if keywords:
            posts = Post.objects.filter(title__contains=keywords)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
