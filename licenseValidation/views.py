from django.shortcuts import render
from .models import DriverLicense
from django.http import HttpResponse

def verify_license(request):
    if request.method == 'GET':
        license_number = request.GET.get('license_number')
        try:
            license = DriverLicense.objects.get(license_number=license_number)
            context = {'license': license}
        except DriverLicense.DoesNotExist:
            context = {'error': 'License not found'}
        return render(request, 'licenses/verify_license.html', context)

def license_status(request):
    if request.method == 'GET':
        license_number = request.GET.get('license_number')
        try:
            license = DriverLicense.objects.get(license_number=license_number)
            status = license.status
            return HttpResponse(f"License status: {status}")
        except DriverLicense.DoesNotExist:
            return HttpResponse("License not found")
