import requests
from celery import shared_task

from apps.scanner.models import IPAddress


@shared_task
def process_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_obj, _ = IPAddress.objects.get_or_create(address=ip_address)
    ip_obj.info = response.json()
    ip_obj.save()
