from rest_framework import serializers
from .models import Category, Details, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'id',
            'description',
            'composition',
            'contraindication',
            'usage',
            'elimination',            
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = False, read_only = True)
    class Meta:
        model = Product
        fields = [
            'id',
            'objects',
            'name',
            'category',
            'imageUrl',
            'rating',
        ]


class ProductFullSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = False, read_only = True)
    details = DetailsSerializer(many = False, read_only = True)
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