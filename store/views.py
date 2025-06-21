from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# ✅ الصفحة الرئيسية - تعرض index.html وتحتوي على قائمة المنتجات
def main_home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'products': products})

# ✅ صفحة المنتجات المستقلة
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/product_list.html', {'products': products})

# ✅ أضف منتج إلى السلة (باستخدام session)
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart
    return redirect('main_home')

# ✅ عرض صفحة السلة
def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'store/cart.html', {'products': products})
