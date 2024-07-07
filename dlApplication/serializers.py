from rest_framework import serializers
from .models import NewApplication
from .models import LicenseRenewal
from .models import LicenseReissue
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = '__all__'

class NewApplicationSerializer(serializers.ModelSerializer):
    model = NewApplication
    fields = '__all__'


class RenewalSerializer(serializers.ModelSerializer):
    model = LicenseRenewal
    fields = '__all__'


class ReissueSerializer(serializers.ModelSerializer):
    model = LicenseReissue
    fields = '__all__'

