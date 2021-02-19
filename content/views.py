from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import UserForm


def home(reqest):
    form = UserForm()
    return render(reqest, 'content/index.html', {'form': form})


def contacts(reqest):
    return render(reqest, 'content/contacts.html')