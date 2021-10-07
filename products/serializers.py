from rest_framework import serializers
from .models import Product, ProductDetails


class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetails
        fields = [
            'id',
            'description',
            'composition',
            'contraindication',
            'usage',
            'elimination',            
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # details = ProductDetailsSerializer(many = False, read_only = True)
    details = serializers.PrimaryKeyRelatedField(many = False, read_only = True)
    class Meta:
        model = Product
        fields = [
            'id',
            'objects',
            'name',
            'category',
            'imageUrl',
            'rating',
            'details',
        ]