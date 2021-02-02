from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Shop_main.as_view()),
    path('<slug>', views.Shop_detail_page.as_view(), name='shop_detail')
]