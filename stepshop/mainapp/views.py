from django.shortcuts import render

from mainapp.models import Product,ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Home', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About Us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contact Us', 'route': 'contact/'},
]


def products(request):
    products_ = Product.objects.all().order_by('price')
    categories = ProductCategory.objects.all()

    context = {
        'title': 'products',
        'links_menu': links_menu,
        'products': products_,
        'categories': categories,
    }
    return render(request, 'products.html', context)


def product(request):
    context = {
        'title': 'product',
        'links_menu': links_menu
    }
    return render(request, 'product.html', context)
