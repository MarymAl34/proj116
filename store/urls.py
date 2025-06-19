# store/urls.py
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='home'),           # الصفحة الرئيسية تعرض المنتجات
    path('products/', views.product_list, name='product_list'),  # قائمة المنتجات بشكل صريح
]
