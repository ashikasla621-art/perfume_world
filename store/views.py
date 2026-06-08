from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Brand, Product, Order, OrderItem, UserProfile
from .cart import Cart
from decimal import Decimal

def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    featured_products = Product.objects.filter(is_featured=True)[:8]
    if not featured_products.exists():
        featured_products = Product.objects.all()[:8]
    
    # Custom blog simulation since we don't need a heavy blog app
    blogs = [
        {
            'id': 1,
            'title': 'Best Perfume Brands in 2025',
            'date': '29 June',
            'description': 'Perfume in 2025 is being shaped by sustainability, inclusivity, and bold scent experiments (matcha, gourmand, woods). Read more to find your brand.',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001358_Top-10-perfume-brands-for-male-cover_1024x1024_300.webp'
        },
        {
            'id': 2,
            'title': 'How to Properly Apply Perfumes',
            'date': '29 June',
            'description': 'Fragrance is a personal statement. The right method can make your perfume last twice as long. Learn the secret spots!',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001351_GettyImages_114848683_300.webp'
        },
        {
            'id': 3,
            'title': 'Customer Service Excellence',
            'date': '29 June',
            'description': 'Discover our commitment to original fragrances and world-class customer service across our physical outlets and online platform.',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001013_0000393_300.jpeg'
        }
    ]

    context = {
        'categories': categories,
        'brands': brands,
        'featured_products': featured_products,
        'blogs': blogs
    }
    return render(request, 'store/home.html', context)

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    # Searching
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(category__name__icontains=query)
        )

    # Filtering
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    brand_slug = request.GET.get('brand')
    if brand_slug:
        products = products.filter(brand__slug=brand_slug)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=Decimal(min_price))
    if max_price:
        products = products.filter(price__lte=Decimal(max_price))

    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'rating':
        products = products.order_by('-rating')
    else:
        products = products.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
        'selected_category': category_slug,
        'selected_brand': brand_slug,
        'query': query,
        'sort_by': sort_by,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'store/shop.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    # Simple mock reviews
    reviews = [
        {'user': 'Adnan Ahmed', 'rating': 5, 'date': 'June 1, 2026', 'comment': 'Absolutely divine fragrance! The packaging was great and it is 100% original.'},
        {'user': 'Nabila Rahman', 'rating': 4, 'date': 'May 28, 2026', 'comment': 'Lasts about 6-8 hours. Very premium scent, perfect for evening wear.'}
    ]

    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews
    }
    return render(request, 'store/detail.html', context)

def cart_detail(request):
    return render(request, 'store/cart.html')

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override', False)
    cart.add(product=product, quantity=quantity, override_quantity=override)
    messages.success(request, f"{product.name} added to cart.")
    return redirect('store:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f"{product.name} removed from cart.")
    return redirect('store:cart_detail')

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, override_quantity=True)
    return redirect('store:cart_detail')

@login_required(login_url='store:login')
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('store:shop')

    profile = request.user.profile
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        if not name or not phone or not address:
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'store/checkout.html')

        # Create Order
        order = Order.objects.create(
            user=request.user,
            shipping_name=name,
            shipping_phone=phone,
            shipping_address=address,
            payment_method=payment_method,
            total_amount=cart.get_total_price(),
            is_paid=False,
            status='Pending'
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )

        if payment_method == 'SSLCommerz':
            return redirect('store:payment_portal', order_id=order.id)
        else:
            cart.clear()
            messages.success(request, "Order placed successfully! Thank you for shopping with us.")
            return redirect('store:order_confirmation', order_id=order.id)

    return render(request, 'store/checkout.html', {'profile': profile})

@login_required(login_url='store:login')
def payment_portal(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.is_paid:
        return redirect('store:order_confirmation', order_id=order.id)

    if request.method == 'POST':
        gateway = request.POST.get('gateway') # bkash, nagad, rocket, card
        order.is_paid = True
        order.status = 'Processing'
        order.save()
        
        # Clear Cart
        cart = Cart(request)
        cart.clear()

        messages.success(request, f"Payment successful via {gateway.upper()}! Thank you.")
        return redirect('store:order_confirmation', order_id=order.id)

    return render(request, 'store/payment.html', {'order': order})

@login_required(login_url='store:login')
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_confirmation.html', {'order': order})

def contact_us(request):
    if request.method == 'POST':
        messages.success(request, "Your message has been sent successfully. We will get back to you shortly.")
        return redirect('store:contact_us')
    return render(request, 'store/contact.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save extra fields in profile if needed
            profile = user.profile
            profile.phone = request.POST.get('phone', '')
            profile.address = request.POST.get('address', '')
            profile.save()

            login(request, user)
            messages.success(request, "Registration successful. Welcome to Perfume World!")
            return redirect('store:home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect(request.GET.get('next', 'store:home'))
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

@login_required(login_url='store:login')
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('store:home')
