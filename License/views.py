from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import License
from .serializers import LicenseSerializer

# Create your views here.

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    lookup_field = 'licenseId'

    @action(detail=True, methods=['get'])
    def status(self, request, licenseId=None):
        try:
            license = self.get_object()
            current_date = timezone.now().date()
            if license.expiry_date < current_date:
                status_message = 'Expired'
            else:
                status_message = 'Valid'
            return Response({'licenseId': licenseId, 'status': status_message})
        except License.DoesNotExist:
                        return Response({'licenseId': licenseId, 'status': 'Fake'}, status=status.HTTP_404_NOT_FOUND)

