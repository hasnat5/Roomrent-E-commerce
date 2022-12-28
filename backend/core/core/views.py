from django.shortcuts import render
from django.views.generic import ListView
from seller.models.Product import Product

def login(request):
    return render(request,'login.html')

