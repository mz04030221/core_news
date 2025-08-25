from django.conf import settings
from django.db import models
from django.urls import reverse


class Issue(models.Model):
    EDITION_CHOICES = [
        ("DAILY", "Daily"),
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
    ]

    title = models.CharField(max_length=250)
    cover = models.ImageField(upload_to="images/")
    edition = models.CharField(
        max_length=250,
        choices=EDITION_CHOICES,
        default="DAILY",
    )
    editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("issue_detail", kwargs={"pk": self.pk})
