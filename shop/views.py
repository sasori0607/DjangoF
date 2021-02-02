from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

def shop_main0(reqest):
    return render(reqest, 'shop/shop.html')

class Shop_main(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products' #ПОД ?
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_main, self).get_context_data(**kwargs)
        ctx['title'] = 'ggg'
        return ctx

class Shop_detail_page(DetailView):
    model = Product
    template_name = 'shop/shop_detail.html'
