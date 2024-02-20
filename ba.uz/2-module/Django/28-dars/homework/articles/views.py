from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")


def articles_view(request):
    return render(request, "articles.html")
