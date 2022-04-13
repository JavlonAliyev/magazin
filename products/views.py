from django.db.models import F, Q
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, ProductTagModel, BrandModel

class ProductsListView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if brand:
            qs = qs.filter(brand_id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if sort:
           if sort == 'price':
               # qs = qs.order_by('get_price')
               qs = sorted(qs, key=lambda i: i.get_price())

           elif sort == '-price':
               # qs = qs.order_by('-get_price')
               qs = sorted(qs, key=lambda i: i.get_price(), reverse = True)


        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        return context

class ProductsDetailView(DetailView):
    template_name = 'shop-details.html'
    model = ProductModel

