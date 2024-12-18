from django.shortcuts import render
from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def checkout(request):

    # Users with accounts - prefill the form

    if request.user.is_authenticated:

        try:

            # Authenticated users with shipping information

            shippping_adress = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shippping_adress}

            return render(request, 'payment/checkout.html', context=context)
        
        except:

            # Authenticated users without shipping information

            return render(request, 'payment/checkout.html')
        
    else:

        return render(request, 'payment/checkout.html')


def payment_success(request):

    for key in list(request.session.keys()):

        if key == 'session_key':

            del request.session[key]

    return render(request, 'payment/payment-success.html')


def payment_failed(request):

    return render(request, 'payment/payment-failed.html')


def complete_order(request):

    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        shipping_address = f"{address1}\n{address2}\n{city}\n{state}\n{zipcode}"

        # Shopping cart information

        cart = Cart(request)

        total_cost = cart.get_total()

        product_list = []

        if request.user.is_authenticated:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost, user=request.user)

            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'], user=request.user)

                product_list.append(f"{item['product']} x {item['qty']}")

        else:

            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost)

            order_id = order.pk

            for item in cart:

                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'])

                product_list.append(f"{item['product']} x {item['qty']}")

        # Email order

        order_details = "\n".join(product_list)
        email_subject = 'Order Received'
        email_body = (
            f"Hi {name},\n\n"
            f"Thank you for placing your order.\n\n"
            f"Shipping Address:\n{shipping_address}\n\n"
            f"Order Details:\n{order_details}\n\n"
            f"Total Paid: ${total_cost}\n\n"
            f"Thank you for shopping with us!"
        )

        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [email], fail_silently=False)

        order_success = True

        response = JsonResponse({'success': order_success})

        return response