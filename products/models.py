'''Products and Variants Models'''
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# ------------------------------
# Base Product
# ------------------------------
class Product(models.Model):
    """Base product information"""

    class ConditionChoices(models.TextChoices):
        '''Documentation String'''
        IN_BOX = "in box", "In Box"
        NEW = "new", "New"
        ALMOST_NEW = "almost new", "Almost New"
        UK_USED = "uk used", "UK Used"
        US_USED = "us used", "US Used"

    # Basic Info
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    # Relations
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE)

    # Product attributes
    condition = models.CharField(max_length=20, choices=ConditionChoices.choices)
    just_in = models.BooleanField(default=False)
    free_gift = models.BooleanField(default=False)
    free_shipping = models.BooleanField(default=False)

    # Discount
    discount = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    # Optional SEO / meta
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.name}"


# ------------------------------
# Product Variants
# ------------------------------
class ProductVariant(models.Model):
    """Each variant of a product (color, storage, RAM, price, stock)"""

    product = models.ForeignKey(
        Product,
        related_name='variants',
        on_delete=models.CASCADE
    )

    # Options
    color = models.CharField(max_length=50)
    storage = models.CharField(max_length=50, null=True, blank=True)
    ram = models.CharField(max_length=50, null=True, blank=True)

    # Pricing & stock
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # Optional image for this variant (overrides main product image)
    image = models.ImageField(upload_to='variants/', null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.color} {self.storage}/{self.ram}"


# ------------------------------
# Product Images / Gallery
# ------------------------------
class ProductImage(models.Model):
    """Additional images for a product (thumbnails, gallery)"""

    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    sub_image = models.ImageField(upload_to='products/gallery/')
    alt_text = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"Image of {self.product.name}"
