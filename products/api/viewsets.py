'''Docstring'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from products.serializers import ProductSerializer #pylint:disable=e0401
from products.models import Product #pylint:disable=e0401

class ProductViewset(ModelViewSet):
    '''Documentation String'''
    permission_classes = [AllowAny]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
