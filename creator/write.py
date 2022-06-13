from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from datetime import timedelta
from flask_mysqldb import MySQL
from sqlalchemy import func, update, desc
from os import path
from requests import get
from socket import inet_aton
from struct import unpack
from json import loads, dumps
import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="ip"
)
sql = mydb.cursor()


with open('./creator/ip.txt', 'r', encoding='utf-8') as f:
    ips = f.read().split('\n')

num = 0
clock = 1000
for ip in ips:
    try:
        array2 = ip.split('";"')
        array = []
        for i in array2:
            i = i.replace('''"''','')
            array.append(i)
        sql.execute(f'''UPDATE v4 SET lon="{array[1]}",lat="{array[2]}",region="{array[3]}",city="{array[4]}",zip="{array[5]}",countryCode="{array[6]}",asn={array[7]} WHERE ip_start = "{array[0].replace('"',"")}"''')
    except Exception as e:
        print(e, f'''UPDATE v4 SET lon="{array[1]}",lat="{array[2]}",region="{array[3]}",city="{array[4]}",zip="{array[5]}",countryCode={array[6]},asn={array[7]} WHERE ip_start = "{array[0].replace('"',"")}"''')

    if num > clock:
        print(clock)
        clock = clock + 1000
        mydb.commit()
    else:
        num = num + 1
mydb.commit()