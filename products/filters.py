'''Documentation String'''
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    '''Documentation String'''
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    category = django_filters.CharFilter(field_name="category_slug",lookup_expr="iexact")
    brand = django_filters.BaseInFilter(field_name="brand_slug",lookup_expr="in")

    class Meta:
        '''Documentation String'''
        model = Product
        fields = {
            'ram': ['exact'],
            'memory': ['exact'],
            'color': ['exact'],
            'condition':['exact'],
            'screen_size':['lte','gte','exact'],
        }
