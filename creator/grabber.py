from unicodedata import decimal
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, update, desc
from os import path
from requests import get
import socket
from struct import unpack
from json import loads, dumps






print('start read')
print('start write')
with open('./ipranges.txt', 'r') as f:
    ips = f.read().split('\n')
with open('./number.txt', 'r') as f:
    number = int(f.read().replace("\n",""))
with open('./number.txt', 'w') as f:
    number2 = number + 45000
    f.write(f"{number2}")

clock = 45001
 
while clock > 0:
    clock = clock -1
    try:
        socket.inet_aton(ips[number])
        ip = ips[number][:-1] + "1"
        answer = get(f'https://ipinfo.io/{ip}?token=5159c29ba4c7e3')
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
        except: countryCode = '0'
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

        with open('./ipfull.txt', 'a', encoding="utf-8") as f:
            f.write(f"{ips[number]},{lon},{lat},{region},{city},{zip},{countryCode},{name},{isp},{org},{website}\n")
        print(number)

    except socket.error:        
        print(f'IP not valid: {ips[number]}')
        


    number = number + 1
