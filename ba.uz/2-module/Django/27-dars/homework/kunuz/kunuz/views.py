from django.shortcuts import HttpResponse


def home_view(request):
    return HttpResponse("<h1>Hello World!</h1>")


def about_view(request):
    return HttpResponse("About page")
