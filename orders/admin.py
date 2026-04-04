'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Order,OrderItem,ShippingAddress

class OrderItemInline(admin.TabularInline):
    '''Documentation String'''
    model = OrderItem
    extra = 0
    readonly_fields = ["product_id", "variant_id", "quantity", "price"]

class ShippingInline(admin.TabularInline):
    '''Documentation String'''
    model = ShippingAddress
    extra = 0

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = [
        "firebase_uid",
        "total_price",
        "status",
        "get_product_ids",
        "get_shipping_email",
        "get_item_details"
    ]

    inlines = [OrderItemInline, ShippingInline]

    def get_product_ids(self, obj):
        '''Documentation String'''
        # Return comma-separated product_ids for this order
        return ", ".join(str(item.product_id) for item in obj.items.all())
    get_product_ids.short_description = "Products"

    def get_shipping_email(self, obj):
        '''Documentation String'''
        # Access related shipping object
        return obj.shipping.email  # or email if you added that field
    get_shipping_email.short_description = "Shipping Email"

    def get_item_details(self, obj):
        '''Documentation String'''
        return "; ".join(
            f"{item.product_id} ({item.variant_id}) x{item.quantity}" 
            for item in obj.items.all()
        )
    get_item_details.short_description = "Items"
