from seller.models.Product import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect

@api_view(['GET','POST'])
def listProduct(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data, many = True)
    if request.method == "POST":
        data.create(
            namaProduct = request.data['namaProduct'],
            keterangan = request.data['keterangan'],
            owner = request.user,
            gambar = request.data['gambar'],
        )
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            data.save()
            serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, product_name):
    data = Product.objects.filter(namaProduct = product_name)
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    if request.method == "POST":
        print("Hello")
    
@api_view(['GET','PUT'])
def updateProduct(request, product_name):
    data = Product.objects.filter(namaProduct = product_name)
    serializer = ProductSerializer(data, many = True)
    if request.method == "PUT":
        data.update(
            namaProduct = request.data['namaProduct']
        )
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            data.save()
            serializer.save()
            return redirect('')
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def deleteProduct(request, product_name):
    data = Product.objects.filter(namaProduct = product_name)
    serializer = ProductSerializer(data, many = True)
    if request.method == "DELETE":
        data.delete()
        return redirect('/product/')
    return Response(serializer.data)