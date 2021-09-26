from rest_framework import serializers
from .models import Product, ProductDetails


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'objects',
            'name',
            'category',
            'imageUrl',
            'rating',
            'details',
        ]


class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetails
        fields = [
            'description',
            'composition',
            'contraindication',
            'usage',
            'elimination',
        ]