import uuid
from django.db import models
from django.utils import timezone

class DriversLicenseApplication(models.Model):
    application_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_motor_cycle = models.BooleanField(default=False)
    is_motor_vehicle = models.BooleanField(default=False)
    certificate_number = models.IntegerField()
    applied_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(NationalId, on_delete=models.CASCADE)
    application_type = models.CharField(max_length=255)
    license_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.application_id)

