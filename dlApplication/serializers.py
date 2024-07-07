# serializers.py

from rest_framework import serializers
from .models import CustomUser, NewApplication, LicenseRenewal, LicenseReissue

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'nin', 'phone_number')

class NewApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewApplication
        fields = ('user', 'first_name', 'middle_name', 'last_name', 'mother_maiden_name', 'gender', 'date_of_birth',
                  'address', 'lga', 'state', 'email', 'phone_number', 'nin', 'passport_photograph',
                  'certificate_number', 'application_type', 'status', 'center_location', 'application_id', 'created_at', 'updated_at')

class RenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseRenewal
        fields = ('applicant', 'license_number', 'license_expiration_date', 'renewal_fee')

class ReissueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseReissue
        fields = ('applicant', 'license_number', 'license_expiration_date', 'reissue_reason', 'reissue_date')
