from seller.models.Product import Product
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from seller.models.Product import Product
from django.views.generic import ListView

def landingPage(request):
    product = Product.objects.all()
    if request.method == "POST":
        kata_kunci = request.POST['search']
        product = Product.objects.filter(namaProduct__contains = kata_kunci) or Product.objects.filter(owner__contains = kata_kunci)
    context = {
        "product":product,
        'id':'939531303994-k8mv59h159lpi72igte2lp51rj7h4p4k.apps.googleusercontent.com'
    }
    return render(request,'buyer/landingPage.html', context)

class ProductListview(ListView):
    model = Product
    ordering = 'namaProduct'