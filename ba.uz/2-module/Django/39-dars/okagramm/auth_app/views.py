from django.shortcuts import render, redirect
from blog.models import MyUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


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
    d = {}
    if request.method == "POST":
        data = request.POST

        firstname = data["firstname"]
        lastname = data["lastname"]
        username = data['username']

        p1 = data["password1"]
        p2 = data["password2"]

        if not User.objects.filter(username=username).exists() and p1 == p2:
            user = User.objects.create(username=username, password=make_password(p1))
            user.save()
            my_user = MyUser.objects.create(user=user)
            my_user.save()
            return redirect('/auth/signin')
        d['error'] = 'User is already exist or password is not same'
    return render(request, 'signup.html')


@login_required(login_url='/signin')
def logout_view(request):
    logout(request)
    return redirect('/auth/signin')
