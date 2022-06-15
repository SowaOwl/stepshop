from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    if request.user.is_authenticated:
        context = {
            'basket': Basket.objects.filter(user=request.user),
        }
        return render(request, 'basketapp/basket.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    _basket = Basket.objects.filter(user=request.user, products=product).first()

    if not _basket:
        _basket = Basket(user=request.user, products=product)

    _basket.quantity += 1
    _basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
