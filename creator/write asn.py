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


with open('./creator/asn.txt', 'r', encoding='utf-8') as f:
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

        sql.execute(f'''INSERT IGNORE INTO asn(id,name,type,org,website) VALUES ({array[0]},"{array[1]}","{array[2]}","{array[3]}","{array[4]}")''')
        
    except Exception as e:
        print(e, f'''INSERT INTO asn(id,name,type,org,website) VALUES ({array[0]},"{array[1]}","{array[2]}","{array[3]}","{array[4]})''')

mydb.commit()