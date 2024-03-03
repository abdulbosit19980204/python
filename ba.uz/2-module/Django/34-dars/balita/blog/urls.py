from django.urls import path

from .views import home_view, about_view, categories_view, contact_view, categories_article

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('categories/', categories_view),
    path('contact/', contact_view),
    path('article/', categories_article)
]
