from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='account_pics/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Account of {self.user.username}"

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
