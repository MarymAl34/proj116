from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'product_image_preview')
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'product_image_preview')

    fieldsets = (
        (_("معلومات المنتج"), {
            'fields': ('name', 'description', 'price', 'image', 'product_image_preview')
        }),
        (_("تفاصيل أخرى"), {
            'fields': ('created_at',)
        }),
    )

    def product_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border:1px solid #ccc;" />',
                obj.image.url
            )
        return _("لا توجد صورة")

    product_image_preview.short_description = _("معاينة الصورة")
