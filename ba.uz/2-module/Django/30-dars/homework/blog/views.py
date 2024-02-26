from django.shortcuts import render

from .models import Articles


# Create your views here.

def home_view(request):
    articles = Articles.objects.all()
    d = {
        "articles": articles[::-1]
    }
    return render(request, 'index.html', context=d)


def blog_view(request):
    articles = Articles.objects.all()
    d = {
        "articles": articles[::-1],
        "message": "Articles are loading...",
    }
    return render(request, "blog.html", context=d)


def blog_info(request, pk):
    article = Articles.objects.get(id=pk)
    d = {
        'article': article
    }
    print(d)
    return render(request, 'blog-single.html', context=d)


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')
