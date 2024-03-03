from django import forms
from django.core.validators import validate_ipv46_address


class IPAddressForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)

    def clean_address(self):
        address_list = self.cleaned_data["address"].split(",")
        cleaned_addresses = []
        for ip in address_list:
            try:
                cleaned_ip = ip.strip()
                validate_ipv46_address(cleaned_ip)
                cleaned_addresses.append(cleaned_ip)
            except forms.ValidationError:
                raise forms.ValidationError(f"{ip.strip()} is not a valid IP address.")
        return cleaned_addresses
