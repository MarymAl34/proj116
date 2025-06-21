from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("اسم المنتج")
    )
    description = models.TextField(
        verbose_name=_("الوصف")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر")
    )
    image = CloudinaryField(
        folder='products/',  # يتم رفع الصورة إلى مجلد "products" في Cloudinary
        null=True,
        blank=True,
        verbose_name=_("صورة المنتج")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإضافة")
    )

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")

    def __str__(self):
        return self.name
