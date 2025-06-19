from django.db import models
from store.models import Product

class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الدفع")
    status = models.CharField(max_length=20, default='pending', verbose_name="الحالة")

    def __str__(self):
        return f"دفع #{self.id} - {self.status}"
