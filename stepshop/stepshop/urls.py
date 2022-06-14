from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from stepshop.views import index, contacts, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
