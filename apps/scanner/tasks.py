import requests
from celery import shared_task

from apps.scanner.models import IPAddress


@shared_task
def process_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_data = response.json()
    ipobject = IPAddress(address=ip_address, info=ip_data)
    ipobject.save()
    return ip_data
