from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from apps.scanner.api.serializers import IPAddressRetrieveSerializer, IPAddressSerializer
from apps.scanner.forms import IPAddressForm
from apps.scanner.models import IPAddress
from apps.scanner.tasks import process_ip, send_notification


class IPAddressViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer

    def create(self, request, *args, **kwargs):
        form = IPAddressForm(request.data)
        if form.is_valid():
            addresses = form.cleaned_data["address"]
            for address in addresses:
                process_ip.delay(address)
                send_notification(address)
            return Response({"message": "IPs are being processed"}, status=status.HTTP_202_ACCEPTED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = IPAddress.objects.all()
        serializer = IPAddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IPAddressRetrieveSerializer(instance)
        return Response(serializer.data)
