from django.db import IntegrityError
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def homepage(request):
    return render(request, 'wbstatistics/homepage.html')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('homepage')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})


def registration(request):
    if request.method == 'GET':
        return render(request, 'wbstatistics/registration.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('userpage')

            except IntegrityError:
                return render(request, 'wbstatistics/registration.html', {'form': UserCreationForm,
                                                                          'error': "Ткое имя пользователя уже есть."})

        else:
            return render(request, 'wbstatistics/registration.html', {'form': UserCreationForm,
                                                                      'error': "Пароли не совпадают"})


def userpage(request):

    return render(request, 'wbstatistics/userpage.html')

# def get_category():
#     url = "https://catalog.wb.ru/catalog/electronic14/catalog?TestGroup=control&TestID=385&appType=1&cat=9468&curr=rub&dest=-3339992&sort=popular&spp=27&uclusters=1"
#
#     headers = {
#         "Accept": "*/*",
#         "Accept-Language": "ru,en;q=0.9",
#         "Connection": "keep-alive",
#         "Origin": "https://www.wildberries.ru",
#         "Referer": "https://www.wildberries.ru/catalog/elektronika/igry-i-razvlecheniya/aksessuary/garnitury",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "cross-site",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36",
#         "sec-ch-ua": 'Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": 'Windows'
#     }
#
#     response = requests.get(url=url, headers=headers)
#     return response.json()
#
#
# def prepare_items(response):
#     products = []
#
#     products_raw = response.get('data', {}).get('products', None)
#     if products_raw is not None and len(products_raw) > 0:
#         for product in products_raw:
#             products.append({
#                 'brand': product.get('brand', None),
#                 'name': product.get('name', None),
#                 'sale': product.get('sale', None),
#                 'priceU': float(product.get('priceU', None)) / 100,
#                 'salePriceU': float(product.get('salePriceU', None)) / 100,
#             })
#     return products


