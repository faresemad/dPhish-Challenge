import requests
from celery import shared_task

from apps.scanner.models import IPAddress


@shared_task
def process_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_data = response.json()
    ipobject = IPAddress(ip_address=ip_address, data=ip_data)
    ipobject.save()
    return ipobject.id
