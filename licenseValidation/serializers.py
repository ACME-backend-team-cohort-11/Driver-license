from rest_framework import serializers
from .models import DriverLicense

class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = ['holder_name', 'license_number', 'issue_date', 'expiration_date', 'status']
