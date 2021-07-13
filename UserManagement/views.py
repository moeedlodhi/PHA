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
from django.core.mail import send_mail, EmailMessage
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
import face_recognition
import cv2
import os
from PHA.settings import BASE_DIR


def facedect(loc):
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:


        MEDIA_ROOT =os.path.join(BASE_DIR)

        loc = (str(MEDIA_ROOT) + loc)
        face_1_image = face_recognition.load_image_file(loc)
        print(loc)
        print(face_1_image)
        print(face_1_image)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

        #

        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        check = face_recognition.compare_faces(face_1_face_encoding, face_encodings)

        print(check)
        if check[0]:
            return True

        else:
            return False

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

        token = Token.objects.get_or_create(user=Account)[0].key
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})


        if Account:
            if Account.is_active:
                print(Account.profile_pic.url)

                if facedect(Account.profile_pic.url):
                    print('am i here?')


                    login(request, Account)
                    data["message"] = "user logged in"
                    data["username"] = Account.username
                    data['id']=Account.id

                    Res = {"data": data, "token": token,}

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
@permission_classes([AllowAny])
def mysqlToPG(request):
    user_role = pd.read_csv('/home/moeed/Downloads/user_roles.csv')
    for key, value in user_role.items():
        pass
    return Response('happy')
