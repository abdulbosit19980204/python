from django.contrib import admin

from blog.models import Post, LikePost, FavoritePost, CommentPost, Category, Notification, MyUser, FollowMyUser

admin.site.register(MyUser)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(LikePost)
admin.site.register(FavoritePost)
admin.site.register(Notification)
admin.site.register(FollowMyUser)
