from django.shortcuts import render, redirect
from blog.models import MyUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


def sign_in_view(request):
    d = {}
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            d['error'] = 'User not found'

    return render(request, 'signin.html', context=d)


def sign_up_view(request):
    return render(request, 'signup.html')


@login_required(login_url='/signin')
def logout_view(request):
    logout(request)
    return redirect('/signin')
