from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import userSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from rest_framework.validators import ValidationError
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



@api_view(['POST'])
def loginView(request):
    nama = request.data['username']
    sandi = request.data['password']
    akun = authenticate(username = nama, password = sandi)
    if akun is not None:
        print(akun.username)
        login(request, akun)
        print("Login Sukses")
        return redirect(f'/account/{akun.username}/')

@login_required(login_url='/auth/login')
def logoutview(request):
    logout(request)
    return redirect('/auth/login/')