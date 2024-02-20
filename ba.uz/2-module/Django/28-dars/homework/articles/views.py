from django.shortcuts import render, HttpResponse

from .models import Articles


def home_view(request):
    return render(request, "home.html")


def articles_view(request):
    articles = Articles.objects.all()
    d = {
        "articles": articles[::-1],
        "message": "Articles are loading...",
    }
    return render(request, "articles.html", context=d)


def article_views(request, article_id):
    articles = Articles.objects.all()
    d = {
        "article": articles[article_id - 1],
        "message": "Article send to front",
    }
    return render(request, "article.html", context=d)


def article_id(request, a_id):
    return HttpResponse("Your request is: " + str(a_id))
