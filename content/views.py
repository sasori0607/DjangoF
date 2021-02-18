from django.shortcuts import render
from django.views.generic import ListView, DetailView



def home(reqest):

    return render(reqest, 'content/index.html')


def contacts(reqest):
    return render(reqest, 'content/contacts.html')