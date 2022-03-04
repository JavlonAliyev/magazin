from django.contrib import admin

from products.models import CategoryModel, BrandModel, ProductTagModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at', 'discount', 'short_description']
    list_filter = [ 'tags', 'category', 'brand', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'tags', 'brand']