'''Documentation String'''
from rest_framework.routers import DefaultRouter
from orders.api.viewsets import OrderViewSet

router = DefaultRouter()
router.register('orders',OrderViewSet,basename='Orders')

urlpatterns = router.urls
