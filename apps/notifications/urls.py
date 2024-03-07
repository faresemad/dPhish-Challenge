from django.urls import path

from apps.notifications.views import index

urlpatterns = [
    path("", index, name="index"),
]
