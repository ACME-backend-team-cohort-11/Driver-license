from rest_framework import serializers
from .models import NewApplication
from .models import LicenseRenewal
from .models import LicenseReissue
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = ('username', 'nin', 'phone_number')


class NewApplicationSerializer(serializers.ModelSerializer):
    model = NewApplication
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'license_type')

class RenewalSerializer(serializers.ModelSerializer):
    model = LicenseRenewal
    fields = ('application', 'renewal_fee', 'expiration_date', 'new_expiration_date')

class ReissueSerializer(serializers.ModelSerializer):
    model = LicenseReissue
    fields = ('application', 'reissue_reason', 'old_license_number', 'new_license_number', 'expiration_date')
