from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer


# Create your views here.

class CardsView(generics.ListAPIView):
    queryset = Card
    serializer_class = CardSerializer
