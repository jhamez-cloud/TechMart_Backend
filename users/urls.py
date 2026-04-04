'''Documentation String'''
from rest_framework.routers import DefaultRouter
from users.api.viewsets import UserProfileViewset


router = DefaultRouter()
router.register('profiles',UserProfileViewset,basename='Profiles')

urlpatterns = router.urls
