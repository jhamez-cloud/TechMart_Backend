'''Documentation String'''
from rest_framework import serializers
from categories.serializers import CategorySerializer
from brands.serializers import BrandSerializer
from .models import Product,ProductVariant,ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = ProductImage
        fields = "__all__"

class ProductVariantSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = ProductVariant
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    variants = ProductVariantSerializer(many="True",read_only="True")
    images = ProductImageSerializer(many="True",read_only="True")
    class Meta:
        '''Documentation String'''
        model = Product
        fields = "__all__"
