# store/views.py
from django.shortcuts import render
from .models import Product

# ✅ الصفحة الرئيسية - تعرض index.html من templates مباشرة
def main_home(request):
    return render(request, 'index.html')

# ✅ صفحة قائمة المنتجات - تعرض جميع المنتجات بالترتيب الأحدث
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products': products
    }
    return render(request, 'store/product_list.html', context)
