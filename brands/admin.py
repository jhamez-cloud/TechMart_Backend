'''Docstring'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Brand

# Register your models here.
@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    '''Docstring'''
    list_display = ('title','slug','brand_type')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('title',)
