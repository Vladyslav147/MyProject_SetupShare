from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomRegisterUser(AbstractUser):
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')

    def __str__(self):
        return self.username