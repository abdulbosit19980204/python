from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, LikePost, CommentPost, MyUser, FollowMyUser


# Create your views here.
@login_required(login_url='auth/signin')
def home_view(request):
    posts = Post.objects.all()[::-1]
    comments = CommentPost.objects.all()
    user = MyUser.objects.filter(user=request.user).first()
    users = MyUser.objects.exclude(user=request.user)

    likes = LikePost.objects.all()
    d = {
        "posts": posts,
        'users': users[:5],
        "user": user,
        "comments": comments,
        "likes": likes,
    }
    return render(request, 'index.html', context=d)


def profile_view(request):
    user_id = request.GET.get('user_id')
    user = MyUser.objects.filter(user_id=user_id).first()
    current_user = MyUser.objects.filter(user=request.user).first()
    posts = Post.objects.filter(author=user)
    follower_count = FollowMyUser.objects.filter(following=user).count()
    following_count = FollowMyUser.objects.filter(follower=user).count()

    if user_id == current_user.user.id:
        actual_user = True
    else:
        actual_user = False
    d = {
        "user": user,
        "actual_user": actual_user,
        "posts": posts,
        "post_count": posts.count(),
        "following_count": following_count,
        "follower_count": follower_count,
    }
    return render(request, 'profile.html', context=d)


def post_upload_view(request):
    if request.method == "POST":
        my_user = MyUser.objects.filter(user=request.user).first()
        post = Post.objects.create(post_image=request.FILES['post_image'], author=my_user)
        post.save()
        return redirect('/')
    return redirect('/')


def post_comment_view(requsts):
    if requsts.method == "POST":
        data = requsts.POST
        message = data["message"]
        post_id = data["post_id"]
        author = MyUser.objects.filter(user=requsts.user).first()
        obj = CommentPost.objects.create(message=message, post_id=post_id, author=author)
        obj.save()
        return redirect('/#{}'.format(post_id))
    return render(requsts, 'index.html')


def post_like_view(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        post_id = data['post_id']
        author = MyUser.objects.filter(user=request.user).first()
        is_liked = LikePost.objects.filter(author=author, post_id=post_id)
        post = Post.objects.filter(id=post_id).first()
        if not is_liked:
            liked = LikePost.objects.create(author=author, post_id=post_id, )
            liked.save()
            post.like_count += 1
            post.save(update_fields=['like_count'])
        else:
            disliked = is_liked.delete()
            post.like_count -= 1
            post.save(update_fields=['like_count'])
        return redirect('/#{}'.format(post_id))
    return render(request, 'index.html')


def following_view(request):
    user_id = request.GET.get('user_id')
    my_user = MyUser.objects.filter(user=request.user).first()
    follow_c = MyUser.objects.filter(id=user_id).first()
    following = FollowMyUser.objects.filter(follower=my_user, following_id=user_id)
    if not following:

        follow = FollowMyUser.objects.create(follower=my_user, following_id=user_id)
        follow.save()
        follow_c.follower_count += 1
        follow_c.save(update_fields=['follower_count'])
    else:
        following.delete()
        follow_c.follower_count -= 1
        follow_c.save(update_fields=['follower_count'])
    return redirect('/')
