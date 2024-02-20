from django.shortcuts import render
from .models import Articles


def home_view(request):
    return render(request, "home.html")


def articles_view(request):
    articles = Articles.objects.all()
    d = {
        "articles": articles,
        "message": "Articles are loading...",
    }
    return render(request, "articles.html", context=d)


def article_views(request):
    return render(request, "article.html")
