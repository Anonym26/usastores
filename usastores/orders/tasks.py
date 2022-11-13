from usastores.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task(bind=True, name='update_novelties_set')
def order_created(*args, **kwargs):
    print('В магазине появилась новинка')
# @app.task()
# def order_created(order_id):
#     """
#     Задача для отправки уведомления по электронной почте при успешном создании заказа.
#     """
#     order = Order.objects.get(id=order_id)
#     subject = 'Order nr. {}'.format(order_id)
#     message = 'Dear {},\n\nВы успешно разместили заказ.\
#                 Номер вашего заказа {}.'.format(order.first_name,
#                                                 order.id)
#     mail_sent = send_mail(subject,
#                           message,
#                           'romanfilkov26@gmail.com',
#                           [order.email])
#     print('Сообщение отправлено на почту')
#     return mail_sent
