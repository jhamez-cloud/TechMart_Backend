'''Documentation String'''
from rest_framework import serializers
from .models import Order, OrderItem, ShippingAddress


class OrderItemSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = OrderItem
        exclude = ['order']


class ShippingSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = ShippingAddress
        exclude = ['order']


class OrderSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    items = OrderItemSerializer(many=True)
    shipping = ShippingSerializer()

    class Meta:
        '''Documentation String'''
        model = Order
        fields = ['id', 'firebase_uid', 'total_price', 'items', 'shipping']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        shipping_data = validated_data.pop('shipping')

        order = Order.objects.create(**validated_data) #pylint:disable=e1101

        # create items
        for item in items_data:
            OrderItem.objects.create(order=order, **item) #pylint:disable=e1101

        # create shipping
        ShippingAddress.objects.create(order=order, **shipping_data) #pylint:disable=e1101

        return order
