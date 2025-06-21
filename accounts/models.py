from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("اسم المستخدم")
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name=_("الاسم الأول")
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name=_("اسم العائلة")
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("البريد الإلكتروني")
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name=_("رقم الجوال")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("موظف إداري")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("مفعل")
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الانضمام")
    )

    class Meta:
        verbose_name = _("مستخدم")
        verbose_name_plural = _("المستخدمون")

    def __str__(self):
        return self.username
