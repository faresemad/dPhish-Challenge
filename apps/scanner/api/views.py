from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from apps.scanner.api.serializers import IPAddressSerializer
from apps.scanner.forms import IPAddressForm
from apps.scanner.models import IPAddress
from apps.scanner.tasks import process_ip


class IPAddressViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer

    @method_decorator(csrf_exempt)
    def create(self, request, *args, **kwargs):
        form = IPAddressForm(request.data)
        if form.is_valid():
            address = form.cleaned_data["address"]
            process_ip.delay(address)
            return Response({"message": "IP is being processed"}, status=status.HTTP_202_ACCEPTED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = IPAddress.objects.all()
        serializer = IPAddressSerializer(queryset, many=True)
        return Response(serializer.data)
