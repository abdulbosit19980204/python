from django.shortcuts import render


# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def categories_view(request):
    return render(request, 'category.html')


def contact_view(request):
    return render(request, 'contact.html')
