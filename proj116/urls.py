from django.contrib import admin
from django.urls import path, include
from store.views import main_home  # ✅ عرض الصفحة الرئيسية index.html

urlpatterns = [
    path('', main_home, name='main_home'),  # ✅ الرابط الرئيسي للموقع

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # روابط التطبيقات مع namespaces
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('store/', include(('store.urls', 'store'), namespace='store')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
]
