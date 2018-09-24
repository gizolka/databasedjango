from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=25,blank=True)
    lastname = models.CharField(max_length=25,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    department = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.email
