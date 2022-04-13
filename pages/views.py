from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm
from posts.models import PostModel
from products.models import ProductModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = ProductModel.objects.order_by('-pk')[:8]
        context['posts'] = PostModel.objects.order_by('-pk')[:3]

        return context


class ContactCreatView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


