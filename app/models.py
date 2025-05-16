from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class Passport(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak!")
    created_ad=models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
