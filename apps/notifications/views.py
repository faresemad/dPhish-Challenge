from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import HttpResponse


def test(request):
    channel_layer = get_channel_layer()
    user = request.user
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",  # Group name
        {
            "type": "notification_message",
            "message": "This is a message from broadcast",
            "user": user.username,
        },
    )
    return HttpResponse("Sent")
