from django.contrib import admin

from blog.models import Post, LikePost, FavoritePost, CommentPost, Category, Notification, MyUser, FollowMyUser


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'like_count', 'post_image', 'author', 'created_at')
    list_display_links = ('id', 'title', 'category', 'like_count', 'post_image', 'author', 'created_at')
    list_filter = ('title', 'author')


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_image', 'follower_count', 'following_count', 'active', 'created_at')
    list_filter = ('user', 'follower_count', 'following_count')


# admin.site.register(MyUser)
admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(LikePost)
admin.site.register(FavoritePost)
admin.site.register(Notification)
admin.site.register(FollowMyUser)
