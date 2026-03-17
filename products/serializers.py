from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer
from brands.serializers import BrandSerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"