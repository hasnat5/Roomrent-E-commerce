from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from ..authentication.serializers import userSerializer
from django.shortcuts import redirect
from django.conf.urls import handler500
from django.core.exceptions import ObjectDoesNotExist
from seller.models.Product import Product


handler500 = "handler.views.handler500"

#@login_required(login_url='../../auth/login')
@api_view(['GET'])
def listUser(request):
    print(User.objects.filter(username = request.user).first())
    if request.user.groups.get() == Group.objects.get(name = "Admin"):
        data = User.objects.all()
        serializer = userSerializer(data, many = True)
        return Response(serializer.data)
    else:
        data = User.objects.filter(username = request.user)
        serializer = userSerializer(data, many = True)
        return Response(serializer.data)

#done
@api_view(['POST'])
def createUser(request):
    if request.method == "POST":
        if request.data['groups'] == "admin" or request.data['groups'] == 1:
            raise ValidationError('Tidak boleh membuat admin')
        elif request.data['groups'] == "seller" or request.data['groups'] == 2:
            akun = User.objects.create_user(
                email = request.data['email'],
                username = request.data['username'],
                password = request.data['password'],
            ).groups.add(2)
            return redirect(f'/account/{akun.username}/')
        elif request.data['groups'] == "buyer" or request.data['groups'] == 3:
            akun = User.objects.create_user(
                email = request.data['email'],
                username = request.data['username'],
                password = request.data['password'],
            ).groups.add(3)
            return redirect(f'/account/{ request.data["username"] }')
        else:
            raise ValidationError("Input tidak valid")
        
        
#done
#@login_required(login_url='../../auth/login')
@api_view(['GET'])
def getUser(request, username):
    if User.objects.get(username = username) is not None:
        data = User.objects.filter(username = username)
        print(data)
        serializer = userSerializer(data, many=True)
        return Response(serializer.data)
    else:
        raise ObjectDoesNotExist(f'{username} tidak tersedia')

from rest_framework.generics import UpdateAPIView

#@login_required(login_url='../../auth/login')
@api_view(['GET','PUT'])
def updateUser(request, username):
    data = User.objects.filter(username = username)
    product = Product.objects.filter(owner = username)
    akun = User.objects.get(username = username)
    print(type(data))
    serializer = userSerializer(data, many=True)
    if request.method == "PUT":
        newuser = akun.username if None else request.data['username']
        first_name = akun.first_name if None else request.data['first_name']
        last_name = akun.last_name if None else request.data['last_name']
        email = akun.email if None else request.data['email']
        data.update(
            username = newuser,
            # first_name = first_name,
            # last_name = last_name,
            # email = email,
        )
        product.update(
            owner = newuser
        )
        serializer = userSerializer(data = data)
        if serializer.is_valid():
            product.save()
            data.save()
            serializer.save()
        username = request.data['username']
        return redirect(f'/account/{username}/')
    return Response(serializer.data)

#done
#@login_required(login_url='../../auth/login')
@api_view(['GET','DELETE'])
def deleteUser(request, username):
    data = User.objects.filter(username = username)
    serializer = userSerializer(data, many=True)
    if request.method == "DELETE":
        data.delete()
    return Response(serializer.data)
