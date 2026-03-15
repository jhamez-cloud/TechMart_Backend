'''Docstring'''
from django.db import models

# Create your models here.
class LaptopBrand(models.Model):
    '''Docstring'''
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    added_at = models.DateTimeField(auto_now_add=True)
