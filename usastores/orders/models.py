from decimal import Decimal

from django.conf import settings
from django.db import models

from shop.models import Product
# валидатор телефонных номеров
from django.core.validators import RegexValidator


class Order(models.Model):
    """
    Класс Order.
    Хранит сведения о клиенте и о статусе заказа.
    """
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='customer',
                                 verbose_name='Заказчик', null=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=False,
                                    verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    paid = models.BooleanField(default=False, verbose_name='Оплата')
    status = models.CharField(max_length=254, default='Ожидает оплаты', verbose_name='Статус заказа')

    class Meta:
        """
        Класс Meta класса Order.
        """
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        """
        Возвращает заказ по id.
        """
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        """
        Определяет общую стоимость товаров, купленных в этом заказе
        """
        total_cost = sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    Класс OrderItem.
    Позволяет хранить продукт, количество и цену, уплаченную за каждый товар.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        """
        Возвращает id заказа.
        """
        return '{}'.format(self.id)

    def get_cost(self):
        """
        Возвращает общую стоимость заказа.
        """
        return self.price * self.quantity

