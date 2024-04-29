# Auth App URLs

from django.urls import path

from .views import signin_view, register_view, logout_view

urlpatterns = [
    path('signin/', signin_view, name='signin', ),
    path('register/', register_view, name='register', ),
    path('logout/', logout_view, name='logout', ),
]
