from django.contrib.auth import authenticate, login
from users.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class Register(View):
    """
    Класс Register. Представление для регистрации пользователей.
    """
    template_name = 'registration/register.html'

    def get(self, request):
        """
        Возвращает форму регистрации пользователя.
        """
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Логика регистрации пользователя.
        """
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
