from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import DriverLicense
from .serializers import *

# Create your views here.

class DriverLicenseViewSet(viewsets.ModelViewSet):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer

    @action(detail=False, methods=['get'], url_path='validate')
    def validate_license(self, request):
        license_number = request.query_params.get('license_number')

        if not license_number:
            return Response({"error": "license_number parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            license = DriverLicense.objects.get(license_number=license_number)
        except DriverLicense.DoesNotExist:
            return Response({"status": "Fake"})

        status_map = {
            DriverLicense.EXPIRED: "Expired",
            DriverLicense.FAKE: "Fake",
            DriverLicense.VALID: "Valid",
        }

        return Response({"status": status_map.get(license.status, "Unknown")})
