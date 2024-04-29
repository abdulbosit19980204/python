from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user/', default='default/user.avif')
    cover_image = models.ImageField(upload_to='user/cover/', default='user/setting/timeline-1.avif')
    follower_count = models.IntegerField(default=0)

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


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    post_image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    like_count = models.IntegerField(default=0)

    write_comment = models.BooleanField(default=True)
    disable_btn_title = models.TextField(max_length=15, default="Disable")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.username


class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class LikePost(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FavoritePost(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    favorited = models.BooleanField(default=False)
    favorited_title = models.TextField(max_length=15, default="Add Favorite")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user.username


class FollowMyUser(models.Model):
    follower = models.ForeignKey(MyUser, related_name='follower_user', on_delete=models.CASCADE)
    following = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    follow = models.BooleanField(default=False)
    follow_title = models.TextField(max_length=15, default="Follow")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.following.user.username


class Notification(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    reporter_user = models.ForeignKey(MyUser, related_name="notified_user", on_delete=models.CASCADE, blank=True,
                                      null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

    message = models.TextField(max_length=200)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
