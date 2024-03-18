from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post, LikePost, CommentPost, MyUser, FollowMyUser


# Create your views here.
@login_required(login_url='auth/signin')
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
