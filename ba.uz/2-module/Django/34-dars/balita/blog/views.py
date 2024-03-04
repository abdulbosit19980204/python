from django.shortcuts import render
from .models import Article, Category

categories = Category.objects.all()


# Create your views here.

def home_view(request):
    categories = Category.objects.all()
    d = {
        "home": "active",
        "categories": categories
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    categories = Category.objects.all()

    d = {
        "about": "active",
        "categories": categories,
    }
    return render(request, 'about.html', context=d)


def categories_view(request, pk):
    articles = Article.objects.filter(category=pk)
    categories = Category.objects.all()
    cat_name = Category.objects.filter(id=pk)
    d = {
        "articles": articles,
        "category": "active",
        "categories": categories,
        "cat_name": cat_name[0]
    }
    return render(request, 'category.html', context=d)


def categories_article(request):
    d = {
        "category": "active",
        "categories": categories,
    }
    return render(request, 'blog-single.html', context=d)


def contact_view(request):
    d = {
        "contact": "active",
        "categories": categories,
    }
    return render(request, 'contact.html', context=d)
