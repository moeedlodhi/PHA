from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import mysql.connector
from mysql.connector import Error
from django.http import JsonResponse
from UserManagement.utils import face_recognize, token_expire_handler
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
from UserManagement.models import Users,user_roles,settings
from societies.models import user_societies,society,sms_log,report_user_process,zones,plot_size,plots,members,member_plots,member_meta,member_activity,payments,letters,contacts
from process.models import process_types,process,process_types_meta,process_comments
from fees.models import installments,documents
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
import face_recognition
import cv2
import os
from PHA.settings import BASE_DIR

        # Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def login_user(request):

        data = {}
        # reqBody = json.loads(request.body)
        username = request.POST['username']

        password = request.POST['password']
        image=request.FILES['image']
        try:

            Account = Users.objects.get(username=username)
        except BaseException as e:
            raise ValidationError({"Error": f'{str(e)}'})

        token, _ = Token.objects.get_or_create(user=Account)
        user_token = token.key
        # is_expired = token_expire_handler(token)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})


        if Account:
            if Account.is_active:
                print(Account.profile_pic.url)

                if face_recognize(Account.profile_pic.url,image):
                    print('am i here?')


                    login(request, Account)
                    data["message"] = "user logged in"
                    data["username"] = Account.username
                    data['id']=Account.id

                    Res = {"data": data, "token": user_token, "is_expired": "yes"}

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

"""Below begins all Postgres Pulls"""

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def user_roles1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM user_roles'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        user_roles.objects.get_or_create(userRoleID=items[0],role=items[1],role_short=items[2],
                                         created_at=items[3],updated_at=items[4])




    return Response('I am happy')

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def superuser(request):
    use=Users.objects.get(id=32,username='moeed_super')
    use.set_password('ufc112233')
    use.is_admin=True
    use.is_superuser=True
    use.is_staff=True
    use.save()
    return Response('Happy')





@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def user1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM users'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        print(items[2])
        role=user_roles.objects.get(userRoleID=items[2])
        use=Users.objects.get_or_create(id=items[0],admin_id=1,
                                    role_id=role,role=role.role_short,
                                    username=items[4],first_name=items[6],
                                    middle_name=items[7],last_name=items[8],
                                    father_name=items[9],husband_name=items[10],
                                    gender=items[11],cnic=items[12],Address=items[13],city=items[14],
                                    email=items[15],mobile_number=items[16],landline_number=items[17],
                                    status=items[19],comments=items[20],created_at=items[22],
                                    updated_at=items[23])
        use[0].set_password('PHA1234')
        use[0].save()



    return Response('I am happy')









@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def user_societies1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM user_societies'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        soc=society.objects.get(id=items[1])
        used=Users.objects.get(id=items[2])
        roled=user_roles.objects.get(id=items[3])
        user_societies.objects.get_or_create(mysqlid=items[0],society_id=soc,
                                             user_id=used,role_id=roled,
                                             status=items[4],created_at=items[5],
                                             updated_at=items[6])




    return Response('I am happy')



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def settings1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM settings'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        set=settings.objects.get_or_create(setting_key=items[2],setting_value=items[3],created_at=items[4],
                                           updated_at=items[5])




    return Response('I am happy')










@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def report_user_proccess_pull(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM report_user_process'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        zep=zones.objects.get(id=items[1])
        soc=society.objects.get(id=items[2])
        user1=Users.objects.get(id=items[3])

        rep=report_user_process.objects.get_or_create(zone_id=zep,society_id=soc,user_id=user1,
                                                      user_role=items[4],total_process=items[5],
                                                      total_pending=items[6],total_approved=items[7],
                                                      total_cancelled=items[8],total_rejected=items[9],
                                                      process_types_total=items[10],created_at=items[11],
                                                      updated_at=items[12])






    return Response('I am happy')


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def process1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM process'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    error=[]
    for items in records:
        used=Users.objects.get(id=items[2])
        soc = society.objects.get(id=items[1])
        try:
            typed=process_types.objects.get(id=items[3])
        except:
            typed=None
        try:
            assigne=Users.objects.get(id=items[4])
        except:
            assigne=None
        try:
            plo=plots.objects.get(mysql_id=items[7])
        except:
            plo=None
        try:
            pay=payments.objects.get(mysql_id=items[5])
        except:
            pay=None



        try:
                        # mem = members.objects.get(mysql_id=items[6])
                        pro = process.objects.get_or_create(mysql_id=items[0], society_id=soc, user_id=used,
                                                        type_id=typed, assigned_to=assigne, payment_id=pay,
                                                        member_id=items[6], plot_id=plo, process_no=items[8],
                                                        plot_no=items[9],
                                                        street_no=items[10], plot_block_no=items[11],
                                                        plot_address=items[12],
                                                        full_name=items[13], cnic=items[14], type=items[15],
                                                        process_data=items[16],
                                                        process_data_back=items[17], status=items[18],
                                                        created_at=items[19],
                                                        updated_at=items[20])
        except ValueError:
                        print(items[0])
                        raise ValidationError('Value Error')






    print(error)
    return Response('Hello world again')





@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def documents1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM documents'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    error=[]
    for items in records:
        soc=society.objects.get(id=items[1])
        try:
            mem=members.objects.get(mysql_id=items[2])
        except:
            mem=None
        try:
            pro=process.objects.get(mysql_id=items[3])
        except:
            pro=None
        doc=documents.objects.get_or_create(id=items[0],mysql_id=items[0],society_id=soc,member_id=mem,process_id=pro,
                                            model=items[4],temp_id=items[5],savedTo=f"{items[6]}{items[5]}",document_type=items[7],
                                            file_name=items[8],file_size=items[9],file_type=items[10],created_at=items[11],
                                            updated_at=items[12])






    print(error)
    return Response('Hello world again')

















@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def process_types1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM process_types'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        pro=process_types.objects.get_or_create(
            type=items[1],created_at=items[2],updated_at=items[3]
        )
    return Response('Hello world again')



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def process_types_meta1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM process_types_meta'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        pro1=process_types.objects.get(id=items[1])
        met=process_types_meta.objects.get_or_create(id=items[0],type_id=pro1,
                                                     meta_key=items[2],
                                                     meta_value=items[3],
                                                     created_at=items[4],
                                                     updated_at=items[5])
    return Response('Hello world again')



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def process_comments1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM process_comments'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    error=[]
    for items in records:
        try:
            pro1=process.objects.get(mysql_id=items[1])
            used=Users.objects.get(id=items[2])
            pro=process_comments.objects.get_or_create(process_id=pro1,user_id=used,user_role=items[3],
                                                   status=items[4],log=items[5],comments=items[6],
                                                   created_at=items[7],updated_at=items[8])
        except:
            error.append(items[1])


    print(error)
    "Error=[55, 55, 55, 55, 55, 55, 55, 69, 70, 72, 87, 108, 108, 100, 101, 127, 135, 218, 134, 235, 266, 292, 299, 291, 319, 265, 363, 368, 362, 364, 366, 365, 367, 191, 440, 459, 564, 405, 693, 694, 695, 720, 721, 927, 928, 965, 966, 928, 928, 928, 979, 980, 980, 981, 982, 983, 984, 985, 986, 987, 989, 988, 991, 990, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1003, 1002, 1000, 1001, 1001, 1005, 1026, 1026, 1052, 1077, 1078, 1079, 1080, 1099, 1080, 1100, 1080, 1099, 1100, 1080, 1099, 1100, 1120, 1119, 1125, 1132, 1006, 1134, 1135, 1137, 1181, 1194, 1202, 1202, 1136, 1203, 1201, 1216, 1235, 1260, 1263, 1271, 1270, 1270, 1271, 1278, 1279, 1280, 1281, 1282, 1282, 1289, 1150, 1294, 2108, 2738, 2738, 2738, 2738, 2737, 2737, 2737, 2737, 2739, 2739, 2739, 2739, 2746, 2756, 2763, 2768, 2904, 2909, 2904, 2904, 2904, 2904, 2909, 2909, 2909, 2909, 3224, 3224, 3225, 3225, 3225, 3224, 3224, 3225, 3225, 3778, 3779, 3777, 3780, 3775, 3764, 3782, 3781, 3783, 3784, 3785, 3788, 3786, 3789]"
    return Response('Hello world again')












@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def plot_size1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM plot_size'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
        soc=society.objects.get(id=items[1])
        plo=plot_size.objects.create(mysql_id=items[0],society_id=soc,size=items[2],size_in_units=items[3],plot_type=items[4],
                                            rate_per_unit=items[5],
                                            price=items[6],
                                            down_payment=items[7],
                                            installment=items[8],
                                            installment_period=items[9],
                                            total_installments=items[10],
                                            development_charges=items[11],
                                            transfer_fees=items[12],
                                            late_installment_surcharges=items[13],
                                            posession_charge=items[14])
    return Response('Hello world again')


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def plots1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM plots'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
            if items[20]=='1' or items[20]==1:
                k=True
            else:
                k=False
            if items[21]=='1' or items[21]==1:
                k2=True
            else:
                k2=False


            soc=society.objects.get(id=items[1])
            plo=plot_size.objects.get(mysql_id=items[2])
            plot=plots.objects.get_or_create(mysql_id=items[0],society_id=soc,plot_size_id=plo,
                                         plot_number=items[4],street_number=items[5],plot_address=items[6],
                                         block_no=items[7],form_no=items[8],vide_no=items[9],
                                         dated=items[10],rate_per_marla=items[11],interest=items[12],
                                         enhancement_cost=items[13],total_cost=items[14],alloted_excess_area=items[15],


                                         plot_quota=items[18],meta_data=items[19],is_alloted=k,
                                         is_possessed=k2,created_at=items[22],updated_at=items[23])

    return Response('Hello world again')

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def members1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM members'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    for items in records:
            if items[24]=='1' or items[24]==1:
                k0=True
            else:
                k0=False
            if items[25]=='1' or items[25]==1:
                k1=True
            else:
                k1=False

            if items[26]=='1' or items[26]==1:
                k2=True
            else:
                k2=False

            if items[27]=='1' or items[27]==1:
                k3=True
            else:
                k3=False

            if items[28]=='1' or items[28]==1:
                k4=True
            else:
                k4=False

            if items[29]=='1' or items[29]==1:
                k5=True
            else:
                k5=False
            if items[30]=='1' or items[30]==1:
                k6=True
            else:
                k6=False
            if items[31]=='1' or items[31]==1:
                k7=True
            else:
                k7=False
            if items[32] == '1' or items[32] == 1:
                k8 = True
            else:
                k8 = False

            if items[33] == '1' or items[33] == 1:
                k9 = True
            else:
                k9 = False

            soc=society.objects.get(id=items[1])
            used=Users.objects.get(id=items[2])
            mem=members.objects.get_or_create(mysql_id=items[0],society_id=soc,user_id=used,
                                              member_plot_id=items[3],membership_no=items[4],society_no=items[5],
                                              full_name=items[6],block=items[7],size=items[8],type=items[9],
                                              corner=items[10],res_com=items[11],first_name=items[12],middle_name=items[13],last_name=items[14],fh_type=items[15],fh_name=items[16],
                                              gender=items[17],cnic=items[18],current_city=items[19],profession=items[20],date_of_birth=items[21],plot_price=items[22],
                                              status=items[23],allotment_letter=k0,possession_letter=k1,digitizing_letter=k2,
                                              is_balloting=k3,is_auction=k4,is_open=k5,is_proxy=k6,is_imported=k7,
                                              is_exemption=k8,is_pgshf=k9,open_date=items[34],comments=items[35],last_activity=items[36],
                                              created_at=items[37],updated_at=items[38])



    return Response('Hello world again')

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def member_plots1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM member_plots'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:
        try:
            if items[8] == '1' or items[8] == 1:
                k1 = True
            else:
                k1 = False
            mem=members.objects.get(mysql_id=items[1])
            plo=plots.objects.get(mysql_id=items[2])
            memp=member_plots.objects.get_or_create(mysql_id=items[0],member_id=mem,plot_id=plo,plot_no=items[3],
                                                    remaining_amount=items[4],next_due_date=items[5],due_date=items[6],
                                                    last_payment_date=items[7],is_active=k1,created_at=items[9],
                                                    updated_at=items[10])
        except:
            errors.append(items[0])
            print(errors)


    '''errors=[5, 13, 14, 19, 23, 410, 547, 833, 948, 999, 1015, 1017, 1021, 1064, 1085, 1091, 1324, 3099, 3100, 3276, 3500, 4716, 4717, 4718, 5323, 5813, 5815, 8114, 8116, 8372, 8425, 8496, 8497, 8498, 9576, 9577, 10561]
 '''

    print(errors)
    return Response('Hello world again')



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def member_meta1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM member_meta'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:
        try:


            mem=members.objects.get(memberID=items[1])
            member_meta.objects.get_or_create(id=items[0],member_id=mem,meta_key=items[2],meta_value=items[3],
                                          created_at=items[4],updated_at=items[5])
        except:
            errors.append(items[1])
    """Errors [5, 14, 14, 14, 21, 25, 25, 25, 125, 179, 412, 549, 549, 549, 549, 835, 950, 1001, 1017, 1019, 1023, 1066, 1087, 1093, 1326, 1551, 1909, 2413, 2446, 2446, 2446, 2447, 2447, 2447, 2448, 
    2448, 2448, 2449, 2449, 2449, 2450, 2450, 2450, 3102, 3103, 3103, 3103, 3279, 3503, 4127, 4719,
     4720, 4721, 5326, 5816, 5818, 9579, 9579, 9579, 950, 950, 950, 950, 9580, 9580, 9580, 1326, 1326, 1326, 1326, 10564]
"""
    print(errors)
    return Response('Hello world again')









@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def member_activity1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM member_activity'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:
        try:

            used=Users.objects.get(id=items[1])
            mem=members.objects.get(mysql_id=items[2])
            memactivity=member_activity.objects.get_or_create(id=items[0],user_id=used,member_id=mem,
                                                              activity=items[3],activity_date=items[4],
                                                              created_at=items[5],updated_at=items[6])

        except:
            errors.append(items[2])
    """"errors=[5, 14, 21, 25, 412, 549, 835, 950, 1001, 1017, 1019, 1023, 1066, 1087, 1093, 1326, 1551, 2413, 2446, 2447, 2448, 2449, 2450, 3102, 3103, 3279, 3503, 4719, 4720, 4721, 5326, 5816, 5818, 9579, 9580, 10564]
"""
    print(errors)
    return Response('Hello world again')




@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def payments1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM payments'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:

            zoned=zones.objects.get(id=items[1])
            soc=society.objects.get(id=items[2])
            try:
                mem=members.objects.get(mysql_id=items[3])
            except:
                mem=None
            pay=payments.objects.get_or_create(mysql_id=items[0],zone_id=zoned,society_id=soc,member_id=mem,order_no=items[4],plot_no=items[5],
                                               street_number=items[6],block_number=items[7],plot_address=items[8],full_name=items[9],cnic=items[10],mobile_no=items[11],
                                                email=items[12],amount=items[13],fee=items[14],total_amount=items[15],otc_payment_token=items[16],otc_payment_token_expiry=items[17],payment_type=items[18],
                                               mode_of_payment=items[19],status=items[20],created_at=items[21],updated_at=items[22])


    return Response('Hello world again')




@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def letters1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM letters'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:
        try:

            soc=society.objects.get(id=items[1])
            used=Users.objects.get(id=items[2])
            if items[19]==1 or items[19]=='1':
                k1=True
            else:
                k1=False

            mem=members.objects.get(mysql_id=items[3])


            let=letters.objects.get_or_create(mysql_id=items[0],society_id=soc,user_id=used,member_id=mem,
                                              type=items[4],vars=items[5],heading=items[6],body=items[7],
                                              issue_date=items[8],sms_code=items[9],sms_code_hash=items[10],
                                              president_barcode=items[11],president_barcode_hash=items[12],
                                              gs_barcode=items[13],gs_barcode_hash=items[14],qr_code=items[15],
                                              qr_code_hash=items[16],rfid_code=items[17],rfid_code_hash=items[18],
                                              is_printed=k1,print_count=items[20],printing_date=items[21],printed_by=items[22],
                                              status=items[23],created_at=items[24],updated_at=items[25])
        except:
            errors.append(items[3])

    "Errors:[549, 2446]"
    print(errors)
    return Response('Hello world again')





@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def installments1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM installments'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:
        try:
            if items[14]==1 or items[14]=='1':
                k1=True
            else:
                k1=False

            soc=society.objects.get(id=items[1])
            plo = plots.objects.get(mysql_id=items[2])
            used=Users.objects.get(id=items[3])
            mem=members.objects.get(mysql_id=items[5])
            inst=installments.objects.get_or_create( mysql_id=items[0],society_id=soc,plot_id=plo,user_id=used,member_id=mem,
                                                    installment_type=items[6],installment_no=items[7],
                                                    installment=items[8],installment_date=items[9],installment_due_date=items[10],
                                                    installment_charges=items[11],late_fee=items[12],late_fee_wave_off=items[13],
                                                    status=k1,payment_date=items[15],comments=items[16],created_at=items[17],updated_at=items[18]
                                                    )



        except:

            errors.append(items[3])

    "Errors:[1, 1, 1, 1, 1, 1, 1, 11, 11, 11, 11, 11, 11, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20, 2, 2, 2, 2, 2, 2, 2, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 2, 2, 2, 2, 2, 2, 2, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]"

    print(errors)
    return Response('Hello world again')



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def contacts1(request):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='ufc',
                                             user='golden',
                                             password='password')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    sqlquery = 'SELECT * FROM contacts'
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    records = cursor.fetchall()
    errors=[]
    for items in records:
        try:
            soc=society.objects.get(id=items[1])
            mem=members.objects.get(mysql_id=items[2])
            con=contacts.objects.get_or_create(mysql_id=items[0],society_id=soc,member_id=mem,parent_id=items[3],address_type=items[4],
                                           contact_type=items[6],contact=items[7],created_at=items[8],updated_at=items[9])
        except:
            errors.append(items[0])


    "Errors=[17, 18, 19, 20, 49, 50, 51, 52, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 86, 87, 88, 89, 104, 105, 106, 107, 108, 298, 299, 300, 301, 402, 403, 404, 405, 515, 516, 517, 518, 751, 752, 753, 754, 1346, 1347, 1348, 1349, 1717, 1718, 1719, 1720, 2294, 2295, 2296, 2297, 2298, 3519, 3520, 3521, 3522, 4018, 4019, 4020, 4021, 4229, 4230, 4231, 4232, 4233, 4301, 4302, 4303, 4304, 4309, 4310, 4311, 4312, 4325, 4326, 4327, 4328, 4519, 4520, 4521, 4522, 4609, 4610, 4611, 4612, 4637, 4638, 4639, 4640, 5673, 5674, 5675, 5676, 6615, 6616, 6617, 6618, 8141, 8142, 8143, 8144, 10641, 10642, 10643, 10644, 10807, 10808, 10809, 10810, 10811, 10812, 10813, 10814, 10815, 10816, 10817, 10818, 10819, 10820, 10821, 10822, 10823, 10824, 10825, 10826, 10827, 10828, 10829, 10830, 10831, 13912, 13913, 13914, 13915, 13916, 13917, 13918, 13919, 13920, 14852, 14853, 14854, 14855, 15788, 15789, 15790, 15791, 18384, 18385, 18386, 18387, 20843, 20844, 20845, 20846, 20847, 20848, 20849, 20850, 20851, 20852, 20853, 20854, 20855, 20856, 20857, 23366, 23367, 23368, 23369, 25507, 25508, 25509, 25510, 25515, 25516, 25517, 25518, 25519, 38384, 38385, 38386, 38387, 38388, 38389, 38390, 38391, 38392, 38393, 43009, 43010, 43011, 43012]"

    print(errors)
    return Response('Hello world again')













@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    print(request.user)
    use=Users.objects.get(username='moeed_super')
    print(use)
    toke=Token.objects.get(user=use)
    print(toke)
    toke.delete()

    return Response('Hello world')
