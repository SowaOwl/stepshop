from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Home', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About Us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contact Us', 'route': 'contact/'},
]


def products(request, pk=None):
    products_ = Product.objects.all()
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all().order_by('price')
            category = {'name': 'All'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': 'products',
            'links_menu': links_menu,
            'products': products_,
            'categories': categories,
            'category': category,
            'basket': basket,
        }

        return render(request, 'products.html', context)

    context = {
        'title': 'products',
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
        'basket': basket,
    }
    return render(request, 'products.html', context)


def product(request):
    context = {
        'title': 'product',
        'links_menu': links_menu
    }
    return render(request, 'product.html', context)
