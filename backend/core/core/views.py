import hashlib
import os
from urllib.parse import urlencode
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.views import SocialLogin 
from django.contrib.auth.models import User
from allauth.account.views import LoginView
import requests

state = hashlib.sha256(os.urandom(1024)).hexdigest()



def get_access_token(code, redirect_uri):
    data = {
        'code': code,
        'client_id': '939531303994-k8mv59h159lpi72igte2lp51rj7h4p4k.apps.googleusercontent.com',
        'client_secret': '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',
        'redirect_uri':redirect_uri,
        'grant_type': 'authorization_code',
    }
    response = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
    response_data = response.json()
    return response_data.get('access_token')

from django.http import HttpResponse

def handle_auth_response(request):
    code = request.GET.get('code')
    redirect_uri = request.GET.get('redirect_uri')
    access_token = get_access_token(code, redirect_uri)
    return HttpResponse(f'Access token: {access_token}')

def index(request):
    print("Ini halaman")
    if request.method == "POST":
        print(request.POST)
        return redirect('https://accounts.google.com/o/oauth2/token')
    return render(request,'socialaccount/login.html')

def redirect_to_google(request):
    access_token = 'your_access_token'
    redirect_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    params = {
        'client_id': '939531303994-k8mv59h159lpi72igte2lp51rj7h4p4k.apps.googleusercontent.com',
        'response_type': 'code',
        'access_type': 'offline',
        'redirect_uri': '/',
        'scope': 'https://www.googleapis.com/auth/userinfo.email',
        'state': state,
        'access_token': access_token,
    }
    redirect_url += '?' + urlencode(params)
    return HttpResponseRedirect(redirect_url)

