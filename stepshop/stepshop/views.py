from django.shortcuts import render


def index(request):
    context = {
        'title': 'main page',
    }

    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'about',
    }
    return render(request, 'about.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
    }
    return render(request, 'contact.html', context)
