from django.url import path

from views import home_view

urlpatterns = [
    path('', home_view)
]
