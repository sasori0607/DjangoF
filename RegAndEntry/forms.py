from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #вариант2

x = 2
if x == 1:
    class UserRegForm(forms.Form):
        email = forms.EmailField(required=True)
        username = forms.CharField(
            label='Введите Логин',
            required=True,
            help_text='Низя вводить',
            widget = forms.TextInput
        )
        password1 = forms.CharField(
            label='Введите Пароль',
            required=True,
            help_text='НУно сложный пасс',
            widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'pass'})
            #attrs это подключения стилей,
            # class от бутстрапа,
            # placeholder это текст подсказка в поле
        )
        password2 = forms.CharField(
            label='Повторите пароль',
            required=True,
            widget = forms.PasswordInput
        )

        class Meta:
            model = User
            fields = ['email']

else:
    class UserRegForm(UserCreationForm):
        email = forms.EmailField(label='you mail', required=True)

        class Meta:
            model = User
            fields = ['username', 'password1', 'password2', 'email']
