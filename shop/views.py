from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *




def shop_main0(reqest):
    return render(reqest, 'shop/shop.html')



class Shop_main(ListView):
    paginate_by = 4 #количество элементов на странице
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_main, self).get_context_data(**kwargs)
        ctx['title'] = 'ggg'
        return ctx


class Shop_detail_page(DetailView):
    model = Product
    template_name = 'shop/shop_detail.html'


class Shop_category(DetailView):
    model = Category
    template_name = 'shop/category.html'
    context_object_name = 'products_category'



    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_category, self).get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        ctx['products'] = Product.objects.all()
        ctx['category'] = Category.objects.all()
        ctx['slug'] = slug
        return ctx


