from django.shortcuts import render


def products(request):
    return render(request, 'products.html')


def product(request):
    return render(request, 'product.html')