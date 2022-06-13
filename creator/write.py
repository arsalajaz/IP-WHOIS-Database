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

token = ["94d06e691b6c2d","98173cc088c4cc","874eaa20b62d13","58ef7567bad2b3","27937e1a43f583","0e96e71dcf1da2","151a7b4db40761","b155b603bbc67d"]
start = 250000
count = 230000

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="ip"
)

sql = mydb.cursor()

sql.execute("select * from v4 order by ip_start;")

ips = sql.fetchall()

num = 0
good = 0
done = 0
api = 0

for x in ips:
  num = num + 1
  if done > count:
      exit(1)
  if num > start:
    if x[4]:
        good = good + 1
    else:
        done = done + 1
        if x[2][-1] == '0':
            ip = x[2][:-1] + "1"
        answer = get(f'https://ipinfo.io/{x[2][:-1] + "1"}?token={token[api]}')
        if api == 6:
            api = 0
        else:
            api = api + 1 

        try:
            lon = loads(answer.text)['loc'].split(',')[0]
        except: lon = '0'
        try:
            lat = loads(answer.text)['loc'].split(',')[1]
        except: lat = '0'
        try:
            region = loads(answer.text)['region']
        except: region = '0'
        try:
            city = loads(answer.text)['city']
        except: city = '0'
        try:
            zip = loads(answer.text)['postal'] 
        except: zip = '0'
        try:
            countryCode =  loads(answer.text)['country']
        except: countryCode = 'ZZ'
        try:
            asn = loads(answer.text)['asn']['asn']
        except: asn = '0'
        try:
            name = loads(answer.text)['asn']['name']
        except: name = '0'
        try:
            isp =  loads(answer.text)['asn']['type']
        except: isp = '0'
        try:
            org = loads(answer.text)['company']['name']
        except: org = '0'
        try:
            website = loads(answer.text)['asn']['domain']
        except: website = '0'
        try:
            with open('C:/Users/Janis/Documents/GitHub/IP-WHOIS-Database/creator/ip2.txt', 'a', encoding="utf-8") as f:
                f.write(f'''"{x[2]}";"{lon}";"{lat}";"{region}";"{city}";"{zip}";"{countryCode}";"{int(asn.replace('AS',''))}"\n''')
            with open('C:/Users/Janis/Documents/GitHub/IP-WHOIS-Database/creator/asn2.txt', 'a', encoding="utf-8") as f:
                f.write(f'''"{int(asn.replace('AS',''))}";"{name}";"{isp}";"{org}";"{website}"\n''')
            print(f'{num}:{good}:{api}: {ip}')
        except Exception as e:
            with open('C:/Users/Janis/Documents/GitHub/IP-WHOIS-Database/creator/error.txt', 'a', encoding="utf-8") as f:
                f.write(f'ERROR: {e} \nVALUES:{x}, {answer.text}')
                print(f'ERROR AT {x}')