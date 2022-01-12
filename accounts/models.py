from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    age = models.PositiveIntegerField(null = True)
    email = models.EmailField(max_length = 254, null = True)
    dob = models.DateField(max_length=8, null = True)
    is_organiser = models.BooleanField(default=False)

