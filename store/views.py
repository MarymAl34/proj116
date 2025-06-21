from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# ✅ الصفحة الرئيسية - تعرض المنتجات داخل index.html
def main_home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'products': products})


# ✅ صفحة قائمة المنتجات المستقلة
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/product_list.html', {'products': products})


# ✅ تفاصيل منتج معين
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


# ✅ أضف منتج إلى السلة (باستخدام الجلسة)
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart
    return redirect('cart_view')


# ✅ عرض المنتجات داخل السلة
def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'store/cart.html', {'products': products})


# ✅ إزالة منتج من السلة
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart
    return redirect('cart_view')
