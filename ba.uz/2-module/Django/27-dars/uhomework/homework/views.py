from django.shortcuts import HttpResponse, render


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')
