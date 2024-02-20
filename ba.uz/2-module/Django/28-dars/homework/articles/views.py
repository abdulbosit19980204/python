from django.shortcuts import render, HttpResponse

from .models import Articles

articles = Articles.objects.all()


def home_view(request):
    return render(request, "home.html")


def articles_view(request):
    d = {
        "articles": articles,
        "message": "Articles are loading...",
    }
    return render(request, "articles.html", context=d)


def article_views(request, article_id):
    d = {
        "article": articles[article_id - 1],
        "message": "Article send to front",
    }
    return render(request, "article.html", context=d)


def article_id(request, a_id):
    return HttpResponse("Your request is: " + str(a_id))
