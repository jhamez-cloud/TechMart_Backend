'''Documentation String'''
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    '''Documentation String'''
    # Filters for ProductVariant fields
    min_price = django_filters.NumberFilter(field_name='variants__price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='variants__price', lookup_expr='lte')
    ram = django_filters.CharFilter(field_name='variants__ram', lookup_expr='exact')
    storage = django_filters.CharFilter(field_name='variants__storage', lookup_expr='exact')
    color = django_filters.CharFilter(field_name='variants__color', lookup_expr='exact')

    # Filters for Product fields
    screen_size__gte = django_filters.NumberFilter(field_name='screen_size', lookup_expr='gte')
    screen_size__lte = django_filters.NumberFilter(field_name='screen_size', lookup_expr='lte')
    condition = django_filters.CharFilter(field_name='condition', lookup_expr='exact')
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    brand = django_filters.BaseInFilter(field_name='brand__slug', lookup_expr='in')

    class Meta:
        '''Documentation String'''
        model = Product
        # ONLY put fields that exist directly on Product
        fields = ['id', 'condition', 'category', 'brand']
