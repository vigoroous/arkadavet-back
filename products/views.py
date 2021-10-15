from rest_framework.filters import OrderingFilter
from .models import Category, Product, Details
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from products.serializers import ProductSerializer, CategorySerializer, DetailsSerializer, ProductFullSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.core.mail import send_mail


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


class FormViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser]

    def create(self, request):
        print(request.data)
        message = [
            'Имя: {}'.format(request.data['name']),
            'Email: {}'.format(request.data['email']),
            'Телефон: {}'.format(request.data['phone']),
            'Заказ: {}'.format(request.data['order']),
        ]
        res = send_mail(
            'Subject here',
            '\n'.join(message),
            'test@localhost',
            ['bodix@localhost'],
            fail_silently=False,
        )
        print(res)
        return Response(res)
