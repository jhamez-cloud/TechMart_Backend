from rest_framework.routers import DefaultRouter
from brands.api.viewsets import BrandViewset

router = DefaultRouter()
router.register("brands",BrandViewset,basename="brand")

urlpatterns = router.urls
