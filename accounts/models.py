from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name=_("رقم الجوال")
    )

    class Meta:
        verbose_name = _("مستخدم")
        verbose_name_plural = _("المستخدمون")

    def __str__(self):
        return self.username
