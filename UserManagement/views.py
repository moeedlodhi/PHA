from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    RedirectView,
    UpdateView,
)
import pandas as pd
from django.shortcuts import render
from rest_framework.response import Response
from django.core.mail import send_mail
import json
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import authentication_classes
from django.views.decorators.csrf import csrf_exempt
from UserManagement.models import Users

# from UserManagement.models import email_user,Users
from django.core.mail import send_mail,EmailMessage
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.exceptions import ValidationError, ParseError
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import threading
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny
from django.contrib.sites.shortcuts import get_current_site
from django.db import IntegrityError
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from UserManagement.utils import face_recognize, token_expire_handler


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def login_user(request):

        data = {}
        reqBody = json.loads(request.body)
        username = reqBody['username']

        password = reqBody['password']
        try:

            Account = Users.objects.get(username=username)
        except BaseException as e:
            raise ValidationError({"Error": f'{str(e)}'})

        token, _ = Token.objects.get_or_create(user=Account)
        user_token = token.key
        is_expired = token_expire_handler(token)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})


        if Account:
            if Account.is_active:
                print(Account.profile_pic.url)

                if face_recognize(Account.profile_pic.url):
                    print('am i here?')


                    login(request, Account)
                    data["message"] = "user logged in"
                    data["username"] = Account.username
                    data['id']=Account.id

                    Res = {"data": data, "token": user_token, "is_expired": is_expired}

                    return Response(Res)
                else:
                    return Response('Invalid user')
            else:
                raise ValidationError({"Error": f'Account not active'})

        else:
            raise ValidationError({"Error": f'Account doesnt exist'})


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    logout(request)
    return JsonResponse({"Message": "User Successfully logout !!!"})


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def is_token_expire(request):
    token = Token.objects.get(user=request.user)
    is_expire = token_expire_handler(token)
    return Response({"is_expire": is_expire})


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def mysqlToPG(request):
    user_role = pd.read_csv('/home/moeed/Downloads/user_roles.csv')
    
    for key, value in user_role.items():
        pass
    return Response('happy')