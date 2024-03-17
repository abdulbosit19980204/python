from django.shortcuts import render
from .models import Post, LikePost, CommentPost, MyUser, FollowMyUser


# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    users = MyUser.objects.all()
    d = {
        "posts": posts,
        'users': users[:5]
    }
    return render(request, 'index.html', context=d)


def setting_view(request):
    return render(request, 'setting.html')


def profile_view(request):
    return render(request, 'profile.html')


def sign_in_view(request):
    return render(request, 'signin.html')


def sign_up_view(request):
    return render(request, 'signup.html')
