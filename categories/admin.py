'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    '''Docstring'''
    list_display = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('id',)
