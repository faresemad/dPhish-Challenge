from rest_framework import serializers

from apps.scanner.models import IPAddress


class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
