from rest_framework import serializers
from .models import DriverLicense

class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = ['full_name', 'license_number', 'issued_date', 'expiry_date', 'status']
