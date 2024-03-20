from django.urls import path

from .views import (home_view, setting_view, profile_view, post_upload_view, post_comment_view,
                    post_like_view, following_view, )

urlpatterns = [
    path('', home_view),
    path('settings/', setting_view),
    # path('signin/', sign_in_view),
    # path('signup/', sign_up_view),
    path('profile/', profile_view),
    path('post/upload/', post_upload_view),
    path('post/comment/', post_comment_view),
    path('post/like/', post_like_view),
    path('user/follow/', following_view),
]
