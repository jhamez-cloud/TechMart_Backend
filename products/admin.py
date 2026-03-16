'''Docstring'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProjectAdmin(ModelAdmin):
    '''Admin for projects'''
    list_display = ('name','slug','category','price','new_price','discount_percentage','stock_left','category','brand','condition')#pylint:disable=c0301
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name','brand','category')
    list_filter = ('category', 'brand','condition','memory','ram')
    list_per_page = 10
    ordering = ('name',)
