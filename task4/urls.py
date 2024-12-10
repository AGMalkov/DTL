from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='game'),
    path('shop/', views.shop_view, name='shop'),
    path('cart/', views.cart_view, name='cart'),
]
