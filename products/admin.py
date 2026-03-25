'''Docstring'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Product
from .models import ProductVariant

# Register your models here.
class ProductVariantInline(admin.TabularInline):
    '''Documentation String'''
    model = ProductVariant
    extra = 0

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    '''Documentation String'''
    inlines = [ProductVariantInline]
    list_display = ('name','slug','category','brand','condition','discount_percentage')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name','brand__name','category__name')
    list_filter = ('category','brand','condition')
