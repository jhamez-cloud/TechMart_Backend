'''Docstring'''
from django.db import models

# Create your models here.
class Category(models.Model):
    '''Docstring'''
    title = models.CharField(max_length=100,default='Mobilephones')
    slug = models.SlugField(unique=True)

    added_at = models.DateTimeField(auto_now_add=True)
