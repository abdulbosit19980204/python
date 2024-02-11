from django.urls import path
from . import views

urlpatterns = [
    path('members/en', views.hello, name='hello'),
    path('members/uz', views.salom, name='salom')
]
