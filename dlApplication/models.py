from django.contrib.auth.models import Group, Permission, AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    nin = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)

    def __str__(self):
        return self.username

class NewApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    mother_maiden_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    lga = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    nin = models.CharField(max_length=20, unique=True)
    passport_photograph = models.ImageField(upload_to='passport_photos/', null=False, blank=False)
    certificate_number = models.CharField(max_length=20)
    application_type = models.CharField(max_length=10, choices=[('New', 'New'), ('Renewal', 'Renewal'), ('Reissue', 'Reissue')])
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Approved', 'Approved'), ('Ready for Printing', 'Ready for Printing')], default='Pending')
    center_location = models.CharField(max_length=100, blank=False, null=False)
    application_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.application_type}'

class LicenseRenewal(models.Model):
    applicant = models.ForeignKey(NewApplication, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, unique=True)
    license_expiration_date = models.DateField()

    def __str__(self):
        return f"{self.applicant.first_name} {self.applicant.last_name} - Driver License Renewal"

class LicenseReissue(models.Model):
    applicant = models.ForeignKey(NewApplication, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    license_expiration_date = models.DateField()
    
    reissue_reason = models.TextField()
    reissue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.first_name} {self.applicant.last_name} - Driver License Reissue"



