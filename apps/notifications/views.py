from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import HttpResponse, render


def send_notification(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            "type": "notification_message",
            "message": "Done Process 8.8.8.8",
        },
    )
    return HttpResponse("Sent")


def index(request):
    return render(request, "notifications/index.html")
