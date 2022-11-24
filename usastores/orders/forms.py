from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """
    Класс OrderCreateForm.
    Форма для создания новых объектов Orders.
    """

    class Meta:
        """
        Класс Meta класса OrderCreateForm.
        """
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'postal_code', 'city']
