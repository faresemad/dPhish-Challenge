from rest_framework import serializers

from apps.scanner.models import IPAddress


class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = ("id", "address", "created_at")
