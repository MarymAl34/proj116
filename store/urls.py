from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # ✅ الصفحة الرئيسية لعرض المنتجات
    path('', views.product_list, name='home'),

    # ✅ قائمة المنتجات
    path('products/', views.product_list, name='product_list'),

    # ✅ تفاصيل منتج واحد
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    # ✅ إضافة منتج إلى السلة
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # ✅ عرض محتوى السلة
    path('cart/', views.cart_view, name='cart'),

    # ✅ إزالة منتج من السلة
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
