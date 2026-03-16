'''Docstring'''
from django.db import models

# Create your models here.
class Brand(models.Model):
    '''Docstring'''

    class BrandType(models.TextChoices):
        '''Docstring'''
        LAPTOP = "laptop","Laptop"
        PHONE = "phone","Phone"
        ACCESSORY = "accessory","Accessory"

    title = models.CharField(max_length=100)
    brand_type = models.CharField(choices=BrandType.choices)
    slug = models.SlugField(unique=True)
