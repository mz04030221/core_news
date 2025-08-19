from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("WRITER", "Writer"),
        ("EDITOR", "Editor"),
    ]

    role = models.CharField(
        max_length=255,
        choices=ROLE_CHOICES,
        default="WRITER",
    )
    verified = models.BooleanField(default=False)
