from django.shortcuts import render
from .models import Skills


def home(request):
    """ Функция для вывода данных из БД на HTML страницу"""
    items = Skills.objects.all()
    return render(request, 'skills/home.html', {'items': items})
