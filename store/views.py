from django.shortcuts import render
from .models import Product

# ✅ الصفحة الرئيسية - تعرض index.html وتحتوي على قائمة المنتجات
def main_home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'products': products})

# ✅ صفحة قائمة المنتجات بشكل مستقل (إذا أردت صفحة خاصة بها)
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/product_list.html', {'products': products})
