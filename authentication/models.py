# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'ADMIN'
    SUBSCRIBER = 'SUBSCRIBER'
  
    ROLE_CHOICES = (
        (ADMIN, 'Administrator'),
        (SUBSCRIBER, 'Subscriber'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
