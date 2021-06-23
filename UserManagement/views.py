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
from django.shortcuts import render
from rest_framework.response import Response
from django.core.mail import send_mail
import json
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from drf_expiring_token.models import ExpiringToken
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


# Create your views here.
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        reqBody = json.loads(request.body)
        username = reqBody['username']

        password = reqBody['password']
        try:

            Account = Users.objects.get(username=username)
        except BaseException as e:
            raise ValidationError({"Error": f'{str(e)}'})

        token = ExpiringToken.objects.get_or_create(user=Account)[0].key
        token1=ExpiringToken.objects.get_or_create(user=Account)[0]
        print(token1.created)
        print(token1.expires)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})


        if Account:
            if Account.is_active:

                login(request, Account)
                data["message"] = "user logged in"
                data["username"] = Account.username
                data['id']=Account.id

                Res = {"data": data, "token": token,}

                return Response(Res)

            else:
                raise ValidationError({"Error": f'Account not active'})

        else:
            raise ValidationError({"Error": f'Account doesnt exist'})