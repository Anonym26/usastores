
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    """
    Класс UserCreationForm. Переопределяет пользователя.
    """
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        """
        Класс Meta класса UserCreationForms.
        """
        model = User
        fields = ('username', 'email')
