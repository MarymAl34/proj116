from django.contrib import admin
from django.urls import path, include
from store.views import main_home  # ✅ عرض الصفحة الرئيسية index.html

urlpatterns = [
    # ✅ الصفحة الرئيسية للموقع
    path('', main_home, name='main_home'),

    # ✅ لوحة تحكم Django
    path('admin/', admin.site.urls),

    # ✅ روابط تطبيق الحسابات (تسجيل دخول / تسجيل حساب / تسجيل خروج)
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # ✅ روابط تطبيق المتجر
    path('store/', include(('store.urls', 'store'), namespace='store')),

    # ✅ روابط تطبيق الدفع
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
]
