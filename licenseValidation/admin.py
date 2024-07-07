from django.contrib import admin
from .models import *

class DriverLicenseAdmin(admin.ModelAdmin):
    list_display = ('holder_name', 'license_number', 'issue_date', 'expiration_date', 'status')
    search_fields = ('holder_name', 'license_number')
    list_filter = ('status',)

# Register your models here.
admin.register(DriverLicense, DriverLicenseAdmin)