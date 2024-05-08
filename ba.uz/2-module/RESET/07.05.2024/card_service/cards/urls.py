from django.urls import path

from .views import CardsView

urlpatterns = [
    path('', CardsView.as_view(), name='cards'),
]
