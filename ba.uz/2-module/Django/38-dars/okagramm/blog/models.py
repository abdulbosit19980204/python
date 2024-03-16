from django.db import models


# Create your models here.

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    user_image = models.ImageField('media/', blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post_image = models.ImageField('media/', blank=True, null=True)


class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class LikePost(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class FollowMyUser(models.Model):
    follower = models.ForeignKey(MyUser, related_name='follower_user', on_delete=models.CASCADE)
    following = models.ForeignKey(MyUser, on_delete=models.CASCADE)
