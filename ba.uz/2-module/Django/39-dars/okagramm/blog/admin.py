from django.contrib import admin
from .models import MyUser, FollowMyUser, Post, CommentPost, LikePost, Notification


# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_display_links = ('id', 'user')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'like_count', 'write_comment', 'created_at')
    list_display_links = ('id', 'author', 'like_count')


admin.site.register(FollowMyUser)
admin.site.register(CommentPost)
admin.site.register(LikePost)
admin.site.register(Notification)
