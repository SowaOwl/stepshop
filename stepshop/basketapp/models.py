from django.db import models

from mainapp.models import Product
from stepshop import settings


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket'
    )

    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='quantity',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='add time',
        auto_now_add=True,
    )
