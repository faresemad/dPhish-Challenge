from django.urls import path

from apps.notifications.views import index, send_notification

urlpatterns = [
    path("", index, name="index"),
    path("send/", send_notification, name="send_notification"),
]
