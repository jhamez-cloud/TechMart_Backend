'''Documentation String'''
from rest_framework import serializers
from categories.serializers import CategorySerializer
from brands.serializers import BrandSerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    class Meta:
        '''Documentation String'''
        model = Product
        fields = "__all__"
