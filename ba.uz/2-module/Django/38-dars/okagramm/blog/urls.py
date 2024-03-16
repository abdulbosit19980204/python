from django.urls import path

from .views import home_view, setting_view, sign_in_view, sign_up_view, profile_view

urlpatterns = [
    path('', home_view),
    path('settings/', setting_view),
    path('signin/', sign_in_view),
    path('signup/', sign_up_view),
    path('profile/', profile_view),

]
