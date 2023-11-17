from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def view_home(request):
    return render(request, 'home.html', locals())


def view_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', locals())


def view_add_product(request):
    products = Product.objects.all()
    return render(request, 'add_product.html', locals())


def view_new_arrivals(request):
    return render(request, 'new_arrivals.html', locals())


def view_callections(request):
    return render(request, 'callections.html', locals())


def view_about_us(request):
    return render(request, 'about_us.html', locals())


def view_blog(request):
    return render(request, 'blog.html', locals())


def view_contact_us(request):
    return render(request, 'contact_us.html', locals())


def view_signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            pass
    return render(request, "signin.html",locals())


def view_dashboard(request):
    return render(request, 'dashboard.html', locals())

def view_logout(request):
    logout(request)
    return redirect('home')