from django.urls import path

from .views import home_view, articles_view, article_views

urlpatterns = [
    path('', home_view),
    path('articles/', articles_view),
    path('articles/article', article_views)
]
