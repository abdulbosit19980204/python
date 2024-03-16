from django.shortcuts import render


# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def setting_view(request):
    return render(request, 'setting.html')


def profile_view(request):
    return render(request, 'profile.html')



def sign_in_view(request):
    return render(request, 'signin.html')


def sign_up_view(request):
    return render(request, 'signup.html')
