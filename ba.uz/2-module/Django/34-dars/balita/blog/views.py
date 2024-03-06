from django.shortcuts import render, redirect
from .models import Article, Category

categories = Category.objects.all()


# Create your views here.

def home_view(request):
    categories = Category.objects.all()
    slider_article = Article.objects.all().order_by('-view_count')[:3]

    d = {
        "home": "active",
        "categories": categories,
        "slider_article": slider_article
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


def article_info(request, pk):
    if request.method == "POST":
        comment = request.POST
        obj = Comments.objects.create(name=comment['name'], email=comment['email'], telegram=comment['telegram'],
                                      comment=comment['comment'], article_id=pk)
        obj.save()
        return redirect()

    detail = Article.objects.filter(id=pk).first()
    detail.view_count += 1
    detail.save(update_fields=['view_count'])
    d = {
        "category": "active",
        "categories": categories,
        "detail": detail
    }
    return render(request, 'blog-single.html', context=d)


def contact_view(request):
    d = {
        "contact": "active",
        "categories": categories,
    }
    return render(request, 'contact.html', context=d)
