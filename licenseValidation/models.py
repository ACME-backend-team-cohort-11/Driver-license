from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date

# Create your models here.

class DriverLicense(models.Model):
    VALID = 'Valid'
    FAKE = 'Fake'
    EXPIRED = 'Expired'

    STATUS_CHOICES = [
        (VALID, 'Valid'),
        (FAKE, 'Fake'),
        (EXPIRED, 'Expired'),
    ]

    holder_name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=100, unique=True)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=VALID)

    def __str__(self):
        return self.license_number

    def is_expired(self):
        return date.today() > self.expiration_date

    def save(self):
        if self.is_expired():
            self.status = self.EXPIRED
        super().save()
