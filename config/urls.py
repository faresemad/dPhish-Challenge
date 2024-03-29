from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# API patterns for Admin
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# API patterns for Local Apps
urlpatterns += [
    path(f"{settings.API_PREFIX}scanner/", include("apps.scanner.api.urls")),
    path(f"{settings.API_PREFIX}notifications/", include("apps.notifications.urls")),
]
