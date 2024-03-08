import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.http import HttpResponse

from apps.scanner.models import IPAddress


def send_notification(ip_address):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            "type": "notification_message",
            "message": f"IP {ip_address} has been processed",
        },
    )

    return HttpResponse("Notification sent!", status=200)


@shared_task
def process_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_data = response.json()
    ipobject = IPAddress(address=ip_address, info=ip_data)
    ipobject.save()
    send_notification(ip_address)
    return ip_data
