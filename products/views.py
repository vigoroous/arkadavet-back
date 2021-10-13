from rest_framework.filters import OrderingFilter
from .models import Category, Product, Details
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from products.serializers import ProductSerializer, CategorySerializer, DetailsSerializer, ProductFullSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['name', 'category', 'rating']


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class DetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    permission_classes = [permissions.AllowAny]


class ProductFullViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    permission_classes = [permissions.AllowAny]
