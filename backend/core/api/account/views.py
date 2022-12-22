from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from ..authentication.serializers import userSerializer
from django.shortcuts import redirect
from django.conf.urls import handler500
from django.core.exceptions import ObjectDoesNotExist

handler500 = "handler.views.handler500"

@login_required(login_url='../../auth/login')
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


@api_view(['POST'])
def createUser(request):
    if request.method == "POST":
        akun = User.objects.create_user(
            email = request.data['email'],
            username = request.data['username'],
            password = request.data['password'],
        )
        if request.data['groups'] == "seller" or request.data['groups'] == 2:
            akun.groups.add(2)
        elif request.data['groups'] == "buyer" or request.data['groups'] == 3 or request.data['groups'] is None:
            akun.groups.add(3)
        else:
            raise ValidationError("Tidak boleh bikin admin")
        
        

@login_required(login_url='../../auth/login')
@api_view(['GET'])
def getUser(request, username):
    if User.objects.get(username = username) is not None:
        data = User.objects.filter(username = username)
        print(data)
        serializer = userSerializer(data, many=True)
        return Response(serializer.data)
    else:
        raise ObjectDoesNotExist(f'{username} tidak tersedia')

@login_required(login_url='../../auth/login')
@api_view(['GET','PUT'])
def updateUser(request, username):
    print(User.objects.get(username = username) is None)
    data = User.objects.filter(username = username)
    serializer = userSerializer(data, many=True)
    if request.method == "PUT":
        data.update(
            username = request.data['username'],
        )
        serializer = userSerializer(data = data)
        if serializer.is_valid():
            data.save()
            serializer.save()
            username = request.data['username']
        username = request.data['username']
        return redirect(f'/account/{username}/')
    return Response(serializer.data)

@login_required(login_url='../../auth/login')
@api_view(['GET','DELETE'])
def deleteUser(request, username):
    data = User.objects.filter(username = username)
    serializer = userSerializer(data, many=True)
    if request.method == "DELETE":
        data.delete()
    return Response(serializer.data)
