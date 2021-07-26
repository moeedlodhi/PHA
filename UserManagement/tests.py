from django.test import TestCase
import mysql.connector
from mysql.connector import Error
from PHA import settings


# Create your tests here.

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
for index,items in enumerate(records):
    try:
        if '||' in items[6]:
            # print(index)
            # print(items[6])
            # print(items[6].split('||'))
            if len(items[6].split('||')[0].split(','))>1:
                print(items[6])
                print(items[6].split('||')[0].split(','))

    except:
        pass
