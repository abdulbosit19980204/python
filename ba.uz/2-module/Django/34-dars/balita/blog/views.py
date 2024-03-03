from django.shortcuts import render


# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def categories_view(request):
    return render(request, 'category.html')


def categories_article(request):
    return render(request, 'blog-single.html')


def contact_view(request):
    return render(request, 'contact.html')
