from django.urls import path

from .views import home_view, articles_view

urlpatterns = [
    path('', home_view),
    path('articles/', articles_view)
]
