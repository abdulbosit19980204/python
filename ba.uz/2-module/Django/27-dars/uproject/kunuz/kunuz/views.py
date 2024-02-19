from django.shortcuts import HttpResponse


def home_view(request):
    return HttpResponse("Hello world!")


def about_view(request):
    return HttpResponse("About page")
