from django.shortcuts import render


def products(request):
    context = {
        'title': 'products',
    }
    return render(request, 'products.html', context)


def product(request):
    context = {
        'title': 'product',
    }
    return render(request, 'product.html', context)