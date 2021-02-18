from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Shop_main.as_view()),
    path('<category>/<slug>', views.Shop_detail_page.as_view(), name='shop_detail'),
    path('<slug>', views.Shop_category.as_view(), name='shop_category')
]