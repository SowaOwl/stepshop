from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Home', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About Us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contact Us', 'route': 'contact/'},
]


def index(request):
    products_ = Product.objects.all()
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'main page',
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
        'basket': basket,
    }

    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'about',
        'links_menu': links_menu,
    }
    return render(request, 'about.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
        'links_menu': links_menu,
    }
    return render(request, 'contact.html', context)
