"""arkadavet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from products import views


router_products = routers.DefaultRouter()
router_products.register(r'base', views.ProductViewSet, basename='product-base')
router_products.register(r'category', views.CategoryViewSet, basename='product-category')
router_products.register(r'details', views.DetailsViewSet, basename='product-details')
router_products.register(r'full', views.ProductFullViewSet, basename='product-full')
router_products.register(r'form', views.FormViewSet, basename='product-form')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(router_products.urls))
]
