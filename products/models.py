from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BrandModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product tag'
        verbose_name_plural = 'product tags'


class ProductModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0)
    short_description = models.TextField()
    long_description = RichTextUploadingField()
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT, related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.RESTRICT, related_name='products')

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'