from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from orders.models import Order #pylint:disable=e0401
from orders.serializers import OrderSerializer #pylint:disable=e0401

class OrderViewSet(ModelViewSet):
    '''Documentation String'''
    permission_classes = [AllowAny]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
