import requests
from celery import shared_task

from apps.scanner.models import IPAddress


@shared_task
def process_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_data = response.json()
    ip_data['ip'] = ip_address
    ip = IPAddress.objects.create(address=ip_address, info=ip_data)
    return ip.id
