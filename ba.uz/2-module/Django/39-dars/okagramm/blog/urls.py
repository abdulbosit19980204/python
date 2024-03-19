from django.urls import path

from .views import home_view, setting_view, profile_view, post_upload_view

urlpatterns = [
    path('', home_view),
    path('settings/', setting_view),
    # path('signin/', sign_in_view),
    # path('signup/', sign_up_view),
    path('profile/', profile_view),
    path('post/upload/', post_upload_view),

]
