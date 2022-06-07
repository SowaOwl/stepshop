from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from authapp.forms import ShopUserLoginForm


def login(reqest):
    context = {
        'title': 'Login On My Site',
        'login_form': ShopUserLoginForm(data=reqest.POST),
    }

    return render(reqest, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
