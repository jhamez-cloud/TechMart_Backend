'''Docstring'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from categories.models import Category #pylint:disable=e0401
from categories.serializers import CategorySerializer #pylint:disable=e0401

class CategoryViewset(ModelViewSet):
    '''Documentation String'''
    permission_classes = [AllowAny]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
