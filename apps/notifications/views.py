from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_notification(ip_address):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            "type": "notification_message",
            "message": f"Done Process {ip_address}"
        },
    )
    return True
