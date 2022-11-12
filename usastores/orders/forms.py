from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """
    Класс OrderCreateForm.
    Форма для создания новых объектов Orderw.
    """

    class Meta:
        """
        Класс Meta класса OrderCreateForm.
        """
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
