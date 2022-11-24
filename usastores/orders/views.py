from django.shortcuts import render
from django.views.generic import ListView

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from django.core.mail import send_mail


def order_show(request):
    orders = Order.objects.filter(customer=request.user)
    orders_item = OrderItem.objects.all()
    context_object_name = 'orders_user'
    context = {
        'orders': orders,
        'orders_item': orders_item
    }
    return render(request, 'orders/orders_user.html', context=context)


def order_create(request):
    """
    Получает текущую корзину из сессии
    и выполняет задачи в зависимости от метода запроса (GET или POST).
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # отправка email
            send_mail(
                'USA STORES',
                f'Dear {order.first_name}!\n'
                f'Ваш заказ успешно оформлен. Номер заказа: {order.id}.\n\n'
                f'Для подтверждения и оплаты заказа с Вами свяжется менеджер по указанному номеру телефона.\n\n\n'
                f'C уважением, USA STORES!',
                None,
                ['romanfilkov26@icloud.com', order.email],
                fail_silently=False,
            )
            # очистка корзины
            cart.clear()
            context = {
                'order': order
            }
            return render(request, 'orders/created.html', context=context)
    else:
        form = OrderCreateForm
    context = {
        'cart': cart,
        'form': form
    }
    return render(request, 'orders/create.html', context=context)
