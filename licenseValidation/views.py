from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DriverLicense
from .serializers import DriverLicenseSerializer

class LicenseListAPIView(APIView):
    def get(self, request, status):
        licenses = DriverLicense.objects.filter(status=status)
        serializer = DriverLicenseSerializer(licenses, many=True)
        return Response(serializer.data)

class ValidLicensesAPIView(LicenseListAPIView):
    def get(self, request):
        return super().get(request, 'valid')

class ExpiredLicensesAPIView(LicenseListAPIView):
    def get(self, request):
        return super().get(request, 'expired')

class FakeLicensesAPIView(LicenseListAPIView):
    def get(self, request):
        return super().get(request, 'fake')
