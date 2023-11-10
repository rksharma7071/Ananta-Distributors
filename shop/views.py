from django.shortcuts import render
from .models import *



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
