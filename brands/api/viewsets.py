'''Documentation String'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from brands.models import Brand #pylint:disable=e0401
from brands.serializers import BrandSerializer #pylint:disable=e0401

class BrandViewset(ModelViewSet):
    '''Documentation String'''
    permission_classes = [AllowAny]

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
