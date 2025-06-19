from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register_view, CustomLoginView

app_name = 'accounts'  # لاستخدام {% url 'accounts:login' %} مثلاً

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),                   # صفحة تسجيل الدخول
    path('register/', register_view, name='register'),                         # صفحة إنشاء حساب
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),  # تسجيل الخروج
]
