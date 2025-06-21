from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('product__name',)
    ordering = ('-timestamp',)

    fieldsets = (
        (_('معلومات الدفع'), {
            'fields': ('product', 'amount', 'status')
        }),
        (_('الوقت'), {
            'fields': ('timestamp',)
        }),
    )
