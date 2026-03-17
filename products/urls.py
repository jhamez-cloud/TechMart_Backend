from rest_framework.routers import DefaultRouter
from products.api.viewsets import ProductViewset

router = DefaultRouter()
router.register("products",ProductViewset,basename="product")

urlpatterns = router.urls
