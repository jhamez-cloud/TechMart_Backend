from rest_framework.routers import DefaultRouter
from categories.api.viewsets import CategoryViewset

router = DefaultRouter()
router.register("categories",CategoryViewset,basename="category")

urlpatterns = router.urls
