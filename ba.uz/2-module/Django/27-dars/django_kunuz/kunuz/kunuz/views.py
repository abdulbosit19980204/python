from django import HttpResponse


def home_page(request):
    return HttpResponse("Hello world!c")
