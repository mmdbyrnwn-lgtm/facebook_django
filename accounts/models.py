from django.db import models
from django.contrib.auth.models import AbstractUser

class nUser(AbstractUser):
    phone_n = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    profile_p = models.ImageField(upload_to='profile_p', default='profile_p.png')