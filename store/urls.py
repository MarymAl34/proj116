# store/urls.py
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # ✅ عرض قائمة المنتجات كصفحة رئيسية للتطبيق
    path('', views.product_list, name='home'),

    # ✅ عرض قائمة المنتجات بشكل صريح
    path('products/', views.product_list, name='product_list'),

    # ✅ إضافة منتج إلى السلة باستخدام المعرف (ID)
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # ✅ صفحة عرض محتوى السلة
    path('cart/', views.cart_view, name='cart'),
]
