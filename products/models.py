'''Docstring'''
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Product(models.Model):
    '''Docstring'''

    class ConditionChoices(models.TextChoices):
        '''Docstring'''
        IN_BOX = "in box","In Box"
        NEW = "new","New"
        ALMOST_NEW = "almost new","Almost New"
        UK_USED = "uk used","UK Used"
        US_USED = "us used","US Used"

    name = models.CharField(max_length=100,default='Samsung Galaxy X6')
    slug = models.SlugField(unique=True,default='Samsung-Galaxy-X6')
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    price = models.FloatField(null=True)
    just_in = models.BooleanField(null=True)
    free_gift = models.BooleanField(null=True)
    #discounts
    discount = models.BooleanField(null=True)
    discount_percentage = models.IntegerField(null=True,validators=[MinValueValidator(0),MaxValueValidator(100)]) #pylint:disable=c0301
    new_price = models.FloatField(null=True)
    #shipping
    free_shipping = models.BooleanField(null=True)
    shipping_fee = models.FloatField(null=True)
    #Stock
    in_stock = models.BooleanField(null=True)
    stock_left = models.IntegerField(null=True)
    #filter options - strings
    category = models.ForeignKey('categories.Category',on_delete=models.CASCADE)
    brand = models.ForeignKey('brands.Brand',on_delete=models.CASCADE)
    condition = models.CharField(max_length=20,choices=ConditionChoices.choices)
    color = models.CharField(max_length=20)
    gpu = models.CharField(max_length=50,null=True)
    #filter options - numbers
    memory = models.IntegerField()
    ram = models.IntegerField()
    screen_size = models.FloatField()

    def __str__(self):
        return f"{str(self.name)}"
