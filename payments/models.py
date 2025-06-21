from django.db import models
from django.utils.translation import gettext_lazy as _
from store.models import Product

class Payment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج")
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("المبلغ")
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الدفع")
    )
    status = models.CharField(
        max_length=20,
        default='pending',
        verbose_name=_("الحالة"),
        choices=[
            ('pending', _('قيد المعالجة')),
            ('completed', _('مكتمل')),
            ('failed', _('فشل')),
        ]
    )

    class Meta:
        verbose_name = _("دفعة")
        verbose_name_plural = _("المدفوعات")

    def __str__(self):
        return f"{_('دفع')} #{self.id} - {self.get_status_display()}"
