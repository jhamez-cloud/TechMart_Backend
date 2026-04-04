'''Documentation String'''
from django.db import models

class Order(models.Model):
    '''Documentation String'''
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('warehouse', 'In Warehouse'),
    ]

    firebase_uid = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    '''Documentation String'''
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping')

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    address = models.CharField()
    apartment = models.CharField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    additional_info = models.TextField()


class OrderItem(models.Model):
    '''Documentation String'''
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    product_id = models.IntegerField()
    variant_id = models.IntegerField()

    color = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)

    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
