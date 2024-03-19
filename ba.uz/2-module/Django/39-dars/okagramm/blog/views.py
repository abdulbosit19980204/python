from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, LikePost, CommentPost, MyUser, FollowMyUser


# Create your views here.
@login_required(login_url='auth/signin')
def home_view(request):
    posts = Post.objects.all()
    user = MyUser.objects.filter(user=request.user).first()
    users = MyUser.objects.exclude(user=request.user)
    d = {
        "posts": posts,
        'users': users[:5],
        "user": user,
    }
    return render(request, 'index.html', context=d)


def setting_view(request):
    return render(request, 'setting.html')


def profile_view(request):
    return render(request, 'profile.html')


def post_upload_view(request):
    if request.method == "POST":
        my_user = MyUser.objects.filter(user=request.user).first()
        post = Post.objects.create(post_image=request.FILES['post_image'], author=my_user)
        post.save()
        return redirect('/')
    return redirect('/')
