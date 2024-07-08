from django.db import models

class DriverLicense(models.Model):
    full_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('valid', 'Valid'),
        ('expired', 'Expired'),
        ('fake', 'Fake'),
    ])

    def __str__(self):
        return f"{self.license_number} - {self.full_name}"
