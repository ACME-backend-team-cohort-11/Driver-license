from django.db import models
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    idNo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username

class License(models.Model):
    IdNo = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    licenseId = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField()
    passport_photo = models.ImageField(upload_to='passport_photos/', null=False, blank=False)

    def __str__(self):
        return self.licenseId

