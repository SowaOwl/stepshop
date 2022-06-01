from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='description',
        blank=True,
    )

    def __str__(self):
        return self.name or f'Category with id - {self.pk}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
