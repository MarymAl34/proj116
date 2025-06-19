from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('product__name',)
