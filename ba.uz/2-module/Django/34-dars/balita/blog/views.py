from django.shortcuts import render
from .models import Article, Category


# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def categories_view(request):
    articles = Article.objects.all()
    d = {
        "articles": articles
    }
    return render(request, 'category.html', context=d)


def categories_article(request):
    return render(request, 'blog-single.html')


def contact_view(request):
    return render(request, 'contact.html')
