from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST) # если хотим стандарт то UserCreationForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был создан!')
            return redirect('home')
    else:
        form = UserRegForm()

    return render(request, 'RegAndEntry/register.html', {'form' : form})