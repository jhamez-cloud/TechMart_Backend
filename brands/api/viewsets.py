from rest_framework.viewsets import ModelViewSet
from brands.models import Brand #pylint:disable=e0401
from brands.serializers import BrandSerializer #pylint:disable=e0401

class BrandViewset(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer