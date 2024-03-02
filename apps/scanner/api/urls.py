from rest_framework.routers import DefaultRouter

from apps.scanner.api.views import IPAddressViewSet

router = DefaultRouter()
router.register(r"ip-addresses", IPAddressViewSet, basename="ip-address")

urlpatterns = router.urls
