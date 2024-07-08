from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    nin = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)

    def __str__(self):
        return self.username

