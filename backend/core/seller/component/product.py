from ..forms.addProduct import addProductForm, addProductImage
from ..models.Product import Product
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
import requests

def listProduct(request):
    product = Product.objects.all()
    if request.method == "POST":
        kata_kunci = request.POST['search']
        product = Product.objects.filter(
            namaProduct__contains = kata_kunci
            ) or Product.objects.filter(
            owner__contains = kata_kunci
            )
    context = {
        "heading":"List",
        "product":product,
    }
    return render(request,'seller/listProduct.html',context)

def getProduct(request, id_product):
    product = Product.objects.filter(id = id_product)
    gambar = Product.objects.get(id = id_product).gambar
    context = {
        "heading":"List",
        "product":product,
        "img":gambar,
    }
    return render(request,'seller/listProduct.html',context)

def addProduct(request):
    form = addProductForm(request.POST or None, request.FILES)
    formImage = addProductImage(request.POST or None,request.FILES)
    context = {
        "heading":"Add Product",
        "form":form,
        "formImage":formImage,
    }
    if request.method == "POST":
        
        if form.is_valid() and formImage.is_valid():
            Product.objects.all().create(
                namaProduct = request.POST['namaProduct'],
                keterangan = request.POST['keterangan'],
                owner = request.user,
                gambar = request.FILES['gambar']
            )
            return redirect('list')
        else:
            print("tidak valdi")
    return render(request,'seller/addProduct.html',context)

def updateProduct(request, update_id):
    akun = Product.objects.get(id = update_id)
    data = {
        "namaProduct":akun.namaProduct,
        "keterangan":akun.keterangan,
        "owner":akun.owner,
    }
    form = addProductForm(request.POST or None, initial=data, instance=akun)
    image = addProductImage(request.POST or None,request.FILES, initial=data, instance=akun)
    context = {
        "heading":"Update",
        "form":form,
        "formImage":image
    }
    if request.method == "POST":
        if form.is_valid():
            image.save()
            form.save()
            return redirect('list')
    return render(request,'seller/addProduct.html',context)

def deleteProduct(request, delete_id):
    Product.objects.filter(id = delete_id).delete()
    return redirect('list')