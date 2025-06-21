from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import main_home  # ✅ عرض الصفحة الرئيسية index.html

urlpatterns = [
    # ✅ الصفحة الرئيسية للموقع
    path('', main_home, name='main_home'),

    # ✅ لوحة تحكم Django
    path('admin/', admin.site.urls),

    # ✅ روابط تطبيق الحسابات
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # ✅ روابط تطبيق المتجر
    path('store/', include(('store.urls', 'store'), namespace='store')),

    # ✅ روابط تطبيق الدفع
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
]

# ✅ دعم عرض ملفات الوسائط (مثل صور المنتجات) أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
