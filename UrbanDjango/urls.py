"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from task4 import views

def home_view(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task4/', include('task4.urls')),
    path('', views.index_view, name='game'),
    # path('task2/', include('task2.urls')),
    # path('task3/', include('task3.urls')),
    # #path('', home_view, name='home'),
    # path('', views.index_view, name='game'),
    # path('shop/', views.shop_view, name='shop'),
    # path('cart/', views.cart_view, name='cart'),
]
