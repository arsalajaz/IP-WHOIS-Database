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

token = "28f52b79d9c6d2"
start = 0
count = 45000

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

for x in ips:
  num = num + 1
  if done > count:
      exit(1)
  if num > start:
    if x[4]:
        good = good + 1
    else:
        done = done + 1
        ip = x[2][:-1] + "1"
        answer = get(f'https://ipinfo.io/{x[2][:-1] + "1"}?token={token}')
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
            sql.execute(f'''INSERT IGNORE INTO asn(id, name, type, org, website) VALUES  ({int(asn.replace('AS',''))},"{name}","{isp}","{org}","{website}")''')
            sql.execute(f'''UPDATE v4 SET lon="{lon}",lat="{lat}",region="{region}",city="{city}",zip="{zip}",countryCode="{countryCode}",asn={int(asn.replace('AS',''))} WHERE decimal_start = {x[0]}''')
            mydb.commit()
            print(f'{num}:{good}: {ip}')
        except Exception as e:
            with open('C:/Users/Janis/Documents/GitHub/IP-WHOIS-Database/creator/error.txt', 'a', encoding="utf-8") as f:
                f.write(f'ERROR: {e} \nVALUES:{x}, {answer.text}')
                print(f'ERROR AT {x}')