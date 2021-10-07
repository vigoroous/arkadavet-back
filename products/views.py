from .models import Product, ProductDetails
from rest_framework import viewsets
from rest_framework import permissions
from products.serializers import ProductSerializer, ProductDetailsSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
