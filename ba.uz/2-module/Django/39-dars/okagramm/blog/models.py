from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user/', default='default/user.avif')
    follower_count = models.PositiveIntegerField(default=0)
    # first_name = models.CharField(max_length=120, blank=True, null=True)
    # last_name = models.CharField(max_length=120, blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    working_at = models.CharField(max_length=255, blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=True, null=True)

    active = models.BooleanField(default=True)
    who_can_follow = models.BooleanField(default=False)
    show_my_activities = models.BooleanField(default=True)
    search_engines = models.BooleanField(default=True)
    allow_commenting = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.username


class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LikePost(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FollowMyUser(models.Model):
    follower = models.ForeignKey(MyUser, related_name='follower_user', on_delete=models.CASCADE)
    following = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
